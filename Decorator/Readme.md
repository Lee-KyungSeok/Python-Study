# Decorator
  - Decorator 사용법
  - wraps 사용법

---

## Decorator 기본
  ### 1. Decorator 사용 이전
  - 함수를 인자로 받아 새로운 함수를 리턴해주는 함수를 정의해보자
    - 어떤 인자도 받을 수 있도록 `packing`, `Unpacking` 을 이용
    - 이는 함수 시작과 끝을 알려주는 함수!
  - 그 후 특정 함수를 정의하고 처음과 끝을 알려주는 함수에 적용한다.

  ```python
  # 함수의 시작과 끝을 알려주는 함수
  def make_print_start_end(func):
      def new_func(*args, **kwargs):
          print("함수가 시작됩니다.")
          result = func(*args, **kwargs)
          print("함수가 끝났습니다")
          return result
      return new_func

  # 특정 함수 정의
  def print_a_to_b(a, b, c):
      for i in range(a, b, c):
          if i<b:
              print(i, end=', ')
          else:
              print(i)

  # 특정 함수의 시작과 끝을 알기 위해 적용
  newFunc = make_print_start_end(print_a_to_b)
  newFunc(1, 10, 1)

  # 결과
  ## 함수가 시작됩니다.
  ## 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  ## 함수가 끝났습니다.
  ```

  ### 2. Decorator 의 사용
  - 위처럼 계속해서 함수를 받아서 처리하는 것은 가독성이 떨어지고 어렵기 때문에 Decorator 사용
  - Decorator 란?
    - 어떤 동작을 함수의 전/후에 수행해야 하거나, 공통적으로 사용하는 코드를 쉽게 관리하기 위해 사용
    - 하나의 함수를 취해서 또 다른 함수를 반환하는 함수
  - 사용 방법 : `@decorator` 를 함수 위에 붙여준다.
  - 위의 결과와 동일하게 동작한다.

  ```python
  # 함수의 시작과 끝을 알려주는 함수
  def make_print_start_end(func):
      def new_func(*args, **kwargs):
          print("함수가 시작됩니다.")
          result = func(*args, **kwargs)
          print("함수가 끝났습니다")
          return result
      return new_func

  # decorator 사용
  @make_print_start_end_p
  def print_a_to_b_d(a,b,c):
      for i in range(a,b,c):
          if i< b:
              print(i, end=', ')
          else:
              print(i)

  print_a_to_b_d(1, 10, 1)

  # 결과
  ## 함수가 시작됩니다.
  ## 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  ## 함수가 끝났습니다.
  ```

  ### 3. Decorator 의 사용 이유?
  - 공통적으로 사용하는 부분을 따로 떼어낼 수 있다.(ex> 권한체크)
  - 특정 함수들을 테스트할 수 있다(ex> 함수 실행 시간 측정)
    - 이를 통해 알고리즘 공식을 이용하는게 for 문을 이용하는 것보다 훨씬 빠르다는 것을 알 수 있다.
  - 그 외에도 여러가지 존재

  > 에시 - 공통적으로 사용하는 부분을 떼어냄 (권한체크)

  ```python
  ## 공통적으로 사용할 function
  def is_admin(user_name):
      if user_name != 'admin':
          raise Exception("권한이 없습니다.")

  ## 클래스에서 권한 체크
  class Greet(object):
      current_user = None

      @is_admin
      def set_name(self, username):
          self.current_user = username

      @is_admin
      def get_greeting(self, username):
          return "Hello {}".format(self.current_user)
  ```

  > 예시 - 특정 함수들을 테스트 (실행 시간 측정)

  ```python
  ## time 모듈 임포트
  from time import time
  ## 시간 측정 함수 정의
  def make_check_time(func):
      def new_func(*args, **kwargs):
          start_time = time()
          result = func(*args, **kwargs)
          end_time = time()
          print('실행시간 :', end_time-start_time)
          return result
      return new_func

  ## 함수를 실행하고 시간을 측정 2
  @make_check_time
  def sum_1_to_n(n):
      result = 0
      for i in range(1,n+1):
          result +=i
      return result

  ## 함수를 실행하고 시간을 측정 2
  @make_check_time
  def gauss_sum(n):
      return (n*(n+1))/2

  print(sum_1_to_n(100000))
  print(gauss_sum(100000))
  # 결론 => 가우스 공식을 사용하면 연산이 빨라짐
  ```

---

## wrapper
  ### 1. wrapper 사용 이유
  - 데코레이터 내부에서 인자로 전달받은 함수가 익명함수 처럼 취급되어 버리므로 디버깅이 난해해지는 단점이 존재
  - `@wraps` 를 지정하여 decorator를 구현하면 문제없이 해당 함수를 디버깅할 수 있다.

  > 예시

  ```python
  from functools import wraps

  def without_wraps(func):
      def __wrapper(*args, **kwargs):
          return func(*args, **kwargs)
      return __wrapper

  def with_wraps(func):
      @wraps(func)
      def __wrapper(*args, **kwargs):
          return func(*args, **kwargs)
      return __wrapper


  @without_wraps
  def my_func_a():
      """Here is my_func_a doc string text."""
      pass

  @with_wraps
  def my_func_b():
      """Here is my_func_b doc string text."""
      pass
  ```

  > 결과

  ```python
  # Below are the results without using @wraps decorator
  print my_func_a.__doc__
  >>> None
  print my_func_a.__name__
  >>> __wrapper

  # Below are the results with using @wraps decorator
  print my_func_b.__doc__
  >>> Here is my_func_b doc string text.
  print my_func_b.__name__
  >>> my_func_b
  ```
