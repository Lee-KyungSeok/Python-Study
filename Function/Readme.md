# Function
  - Function basic
  - Packing & Unpacking
  - Recursion Function
  - try~ except
  - [몇가지 문제](https://github.com/Lee-KyungSeok/Python-Study/tree/master/Function/Example)

---

## Function basic
  ### 1. function 기초
  - function은 추상화와 분리를 포함시키는 개념
    - 추상화 : 별도에 공간에 존재하여, 변수간 간섭되는 방해를 일으키지 않는 방법
    - 분리 : 코드는 다른곳에 작성되어, 우리가 필요한 경우 호출만 하여 사용할 수 있는 방법
  - def func_name(arg): 후에 아래에 탭키 공백 후 로직 작성
  - 함수 자체를 변수 혹은 리스트, dictionary 에 넣을 수 있다.

  ```Python
  # def func_name(arg):
  #      #코드 작성
  ```
  > 예시 1

  ```Python
  def print_hello_world():
      print("hello world")
      return None # return 이 None이면 없어도 상관 없다.
  print_hello_world()
  ```

  > 예시 2 (함수 중복 사용 가능)

  ```python
  def sum_3(a , b, c):
      return a + b + c
  print(sum_3(1,3,5)) # 출력 : 9
  print(sum_3(1,3, sum_3(4,5,6))) # 출력 : 19
  ```

  > 예시 3 (String 값 출력)

  ```Python
  def add_mark(word):
      return word + "!!!!"
  result_string = add_mark("python")
  print(result_string) # 출력 : python!!!!
  ```

  > 예시 4 (전역변수 이용 가능)

  ```Python
  # 함수 안에 변수가 없다면 함수 이전에 존재하는 전역변수를 참조하게 된다.
  a, b = 3, 4
  def print_other(val):
      a = 1
      return val + a + b
  print(print_other(5)) # 출력 : 10
  ```

  > 예시 4 (input 함수 사용하여 입력 받을 수 있음)

  ```Python
  def number_choice():
      number = int(input("1~9까지 숫자를 입력해주세요"))
      return number
  def multi_2(number):
      return number * 2
  def add_5(number):
      return number + 5

  number = number_choice()
  number = multi_2(number)
  number = add_5(number)
  print(number)
  ```
  
  > 예시 5 (함수를 변수 혹은 리스트, dictionary 에 넣을 수 있다.)

  ```python
  def print_hello(name):
      print("Hello " + name)
      
  print_hello_name = print_hello
  print_hello_name('kyung')
  
  func_list = [print_hello, 1, 2, 3]
  func_list[0]('kyung')

  func_dict = {
      'func' : print_hello,
      'test' : 111
  }
  func_dict['func']('kyung')
  ```

  ### 2. default value
  - 파라미터를 정의 할 때 default 값을 정의할 수 있다.
  - default값이 정의되어 있으면 함수에 파라미터를 넣지 않아도 에러가 발생하지 않는다.
  -  주의 : default value는 항상 뒤에 와야 한다. def function(a=1, b) => 불가능
  - def func_name(value, default value): 로 사용

  > 예시 1

  ```Python
  def add(a, b=1):
      return a + b
  print("a만 입력 :", add(1)) # 출력 : 2
  print("a,b 둘다 입력 :", add(1,5)) # 출력 : 6
  ```

  > 예시 2 (range를 받아 list로 변환하는 함수)

  ```Python
  def range_list(start, end=None, step=None):
      if not end and not step:
          return(list(range(start)))
      elif not step:
          return(list(range(start,end)))
      else:
          return(list(range(start, end, step)))
  print(range_list(10)) # 출력 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(range_list(1,10)) # 출력 : [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(range_list(1,10,2)) # 출력 : [1, 3, 5, 7, 9]
  ```

  ### 3. 위치인자와 키워드인자
  - 위치에 따라 출력될 수 있지만 파라미터의 키워드를 함께 입력해서 다른 위치에서도 넣을 수 있다.
  - 주의 : 위치인자는 항상 키워드인자 앞에 나와야 한다.
  - def func_name(위치인자, 키워드인자): 로 사용

  ```Python
  def test(a, b, c):
      print("a :", a, end=", ")
      print("b :", b, end=", ")
      print("c :", c)
  test(1, 2, 3) # 출력 => a : 1, b : 2, c : 3
  test(b=2, c=4, a=5) # 출력 => a : 5, b : 2, c : 4
  test(3, c=4, b=2) # 출력 => a : 3, b : 2, c : 4
  # test(c=4, b=2, 3) # 이러면 에러를 띄운다 (위치인자는 항상 키워드인자 앞에 나와야 한다.)
  ```
---

## Packing & Unpacking
  ### 1. Packing
  - 위치 인자를 받는 packing
    - \*args 로 표현 (\*는 필수이며 args 는 변수 이름을 관용적으로 표현)
    - 넣은 값들이 tuple 로 들어오게 된다.
  - 키워드 인자를 받는 packing
    - \*\*kwargs 로 표현(\*\*는 필수이며 kwargs 는 변수 이름을 관용적으로 표현)
    - 넣은 값들이 dictionary 형태로 들어오게 된다.

  > 예시 (위치 인자를 받는 packing)

  ```Python
  # 예시 1
  def print_all(*args):
      print(args)
  print_all(1,2,3,4,5,6) # 출력 : (1, 2, 3, 4, 5, 6)

  # 예시 2
  def sum_all(*args):
      return sum(args)
  print(sum_all(1,2,3,4,5,6,7,8,9,10)) # 출력 : 55
  ```

  > 예시 (키워드 인자를 받는 packing)

  ```Python
  # 예시 1
  def print_f_name(**kwargs):
      print(kwargs)
  print_f_name(father = "임꺽정", mother = "김말숙", sister = "둘리", brother = "존", cat = "나비")
  # 출력 : {'father': '임꺽정', 'mother': '김말숙', 'sister': '둘리', 'brother': '존', 'cat': '나비'}

  # 예시 2
  def print_f_name2(**kwargs):
      for key in kwargs:
          print(key, '의 이름은', kwargs[key], '입니다.')
  print_f_name2(father = "임꺽정", mother = "김말숙", sister = "둘리", brother = "존", cat = "나비")
  # 출력
  # father 의 이름은 임꺽정 입니다.
  # mother 의 이름은 김말숙 입니다.
  # sister 의 이름은 둘리 입니다.
  # brother 의 이름은 존 입니다.
  # cat 의 이름은 나비 입니다.
  ```

  ### 2. Unpacking
  - # packing되어 있는 경우 이를 unpacking 하는 개념
  - 함수 호출 할 때 packing과 마찬가지로 \* 혹은 \*\*을 붙여 사용한다.

  > 예시 (위치 인자를 받는 packing)

  ```Python
  # 예시 1
  def print_all_un(*args):
      print(args)
  print_all_un([1,2,3,4,5,6,7,8,9,10]) # 출력 : ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],)
  print_all_un(*[1,2,3,4,5,6,7,8,9,10]) # 출력 : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

  # 예시 2
  def sum_all_un(*args):
      return sum(args)
  # print(sum_all_un([1,2,3,4,5,6,7,8,9,10])) # 출력 : 오류
  print(sum_all_un(*[1,2,3,4,5,6,7,8,9,10])) # 출력 : 55
  ```

  > 예시 (키워드 인자를 받는 packing)

  ```Python
  family_dict = {
      "father" : "임꺽정",
      "mother" : "김말숙",
      "sister" : "둘리",
      "brother" : "존",
      "cat" : "나비"
  }
  def print_f_name_un(**kwargs):
      for key in kwargs:
          print(key, '의 이름은', kwargs[key], '입니다.')
  print_f_name_un(**family_dict)
  # 출력
  # father 의 이름은 임꺽정 입니다.
  # mother 의 이름은 김말숙 입니다.
  # sister 의 이름은 둘리 입니다.
  # brother 의 이름은 존 입니다.
  # cat 의 이름은 나비 입니다.
  ```

  ### 3. 예제
  - 함수를 호출해서 입력 받고싶은 만큼 받고 최종 결과물 호출

  ```Python
  def input_likes():
      likes = []
      while True:
          likes_temp = input("좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력")
          if likes_temp == "exit":
              break
          else:
              likes.append(likes_temp)
      return likes
  def print_likes(*args):
      print(args)
  print_likes(*input_likes())

  # 출력
  # 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력cat
  # 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력dog
  # 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력whale
  # 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력exit
  # ('cat', 'dog', 'whale')
  ```
---

## Recursion Function
  ### 1. Recursion Function
  - 함수 안에서 자신의 함수를 호출

  > 예시 1 (factorial)

  ```Python
  def factorial(n):
      if n==1 or n==0:
          return 1
      else:
          return n * factorial(n-1)
  print(factorial(5)) # 출력 : 120
  ```

  >예시 2 (a와 n을 더하는 함수)

  ```Python
  def add_n(a,n):
      if n==0:
          return a
      return 1 + add_n(a,n-1)
  print(add_n(10, 5)) # 출력 : 15
  ```

---

## 예외처리
  ### 1. 예외처리
  - try, except 를 이용해 에러처리를 한다.
  - 예외처리를 사용할 시 반드시 어떤 에러인지 지정하도록 한다.
  - TypeError(string+int 등), NameError(선언한적 없는 변수 사용), ZeroDivisionError(0으로 나눔) 등 존재

  ```Python
  # 사용법
  # try:
  #     Error 발생할 우려가 있는코드
  # except:
  #     Error 발생시 작동하는 코드
  ```

  > 예시 (값을 입력받아 숫자인지 확인하고 나누는데 0이면 에러처리)

  ```Python
  try:
      # int형이고 0이 아닌경우 경우 여기서 실행
      num = input("숫자를 입력하세요")
      num = int(num)
      print(10/num)
  except ValueError:
      # string으로 입력받게 되면 여기서 실행
      print("숫자키로 입력해주세요")
  except ZeroDivisionError:
      # 0으로 입력받게 되면 여기서 실행
      print("0을 제외하고 입력해주세요")  
  ```
