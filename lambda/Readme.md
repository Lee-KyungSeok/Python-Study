# lambda, sorted, map, filter, reduce
  - lambda
  - sorted
  - map
  - filter
  - reduce

---

## lambda
  ### 1. lambda 기초
  - 함수를 정의하는 것은 동일하지만 들어갈 변수 이름을 지정하지 않음
  - `return` 만 존재하는 함수의 경우 간단하게 나타낼 수 있다.
  - 사용방법 : `lambda (함수에서 받을 값) : (리턴할 값)`
  - 예시

  ```Python
  # x 를 받아 1을 더하는 함수
  lambda x : x + 1
  ```

  ### 2. 특징
  - 람다를 변수에 넣을 수 있다.
  - 람다에 바로 값을 넣어 실행 가능

  ```Python
  # 람다를 변수에 넣음
  a = lambda x, y : x + y
  a(5,8)

  # 람다에 바로 값을 넣어서 실행 가능
  (lambda x, y : x + y)(10, 20)
  ```

  ### 3. 예제
  - 람다식을 이용해서 여러 함수를 만들 수 있다.

  ```python
  # 3개의 값을 더해주는 함수
  lambda x, y, z: x+y+z
  # 2개의 값을 각각 제곱해서 더해주는 함수
  lambda x, y: x**2 + y**2
  # 1개의 숫자를 받아서 2의 배수이면 True, 아니면 False 를 리턴하는 함수
  lambda x : True if x%2==0 else False
  # 0~n개의 정수를 받아서 모두 더해주는 함수
  lambda *args: sum(args)
  ```

---

## sorted
  ### 1. sorted 기초
  - 배열을 정렬해주는 built in 함수
  - 사용 방법 : `sorted(배열, key)`
  - 예시

  ```python
  # 일반 리스트의 경우
  list1 = [4,5,2,5,7,12,3,5,6]
  list2 = ['a','d','b','d','ef','m','vd','f','asdf','eg','h','k']
  sorted(list1)
  sorted(list2)
  ```

  ### 2. dictionary 인 경우
  - 리스트에 `dictionary` 가 있는 경우 정렬한 기준인 `key` 를 지정해 주어야 한다.
  - 이 때 함수를 람다식으로 정해줄 수 있다.

  ```python
  # key 가 존재하는 배열
  students = [
      {
          "first_name": "lee",
          "last_name": "seok",
          "student_no": 3498
      },
      {
          "first_name": "lee",
          "last_name": "hyun",
          "student_no": 9145
      },
      {
          (...)
      }, (...)
  ]

  # 일반적인 function 사용
  def sort_help(d):
      return d['student_no']
  sorted_students = sorted(students, key=sort_help)

  # lambda식 사용
  sorted_students = sorted(students, key=lambda x: x['student_no']);
  ```

---

## map
  ### 1. map 사용 방법
  - map 은 리스트에 있는 모든 값들을 하나씩 변수로 리턴해서 이를 이용해 작업할 수 있도록 도와주는 built in 함수
  - 사용 방법 : `map(function, a)`

  > 예시 (모든 리스트에 1을 더하는 경우)

  ```python
  # 이전 방법
  result = []
  for el in a:
      result.append(el +1)

  # map 이용
  result = map(lambda x: x+1, a)
  ```

  ### 2. 예제
  - 1~100이 담긴 리스트를 fizzbuzz 하기
    - (3의 배수면 fizz, 5의 배수면 buzz, 15의 배수면 fizzbuzz)

  ```python
  # 리스트 정의
  listEx = (range(1, 100+1))
  # map 이용
  result = map(lambda x: 'fizzbuzz' if x%15==0 else ('fizz' if x%3==0 else ('buzz' if x%5==0 else x)), listEx)
  # 리스트로 만들기
  list(result)
  ```

---

## filter
  ### 1. filter 사용 방법
  - function 리턴값이 `True` 면 값을 넘기고 `False` 면 값을 지운다.
    - 즉, function의 리턴값은 반드시 True / False 여야 한다.
  - 사용 방법 : `filter(function, list) `

  > 에시 (2의 배수만 거르는 경우)

  ```python
  # 리스트 정의
  a = list(range(1, 10+1))

  # 이전 방법
  result = []
  for el in a:
      if(el % 2 == 0):
          result.append(el)

  # filter 이용
  filterResult = list(filter(lambda x : x%2==0, a))
  ```

  ### 2. 예제
  - 1~100 리스트에서 50보다 큰 값만 남긴 후 2의 배수만 가진 리스트 남기기

  ```python
  # 리스트 정의
  at = list(range(1,100+1))
  # filter 이용
  result = filter(lambda x: x%2==0, (filter(lambda x: x>50, at)) )
  # 리스트로 만들기
  list(result)
  ```

---

## reduce
  ### 1. reduce 사용 방법
  - 리스트를 받아서 하나씩 줄여 하나의 리턴값을 내보낸다.
  - bulit in 함수가 아니므로 `import` 해주어야 한다.
  - 사용 방법 : `reduce(function, list)`

  ```python
  from functools import reduce

  a=list(range(10+1))
  result = reduce(lambda x, y: x+y, a)
  print(result) # 출력 : 55

  # 과정!!!
  ## [0,1,2,3,4,5,6,7,8,9,10] => [1,2,3,4,5,6,7,8,9,10]
  ## => [3,3,4,5,6,7,8,9,10] => [6,4,5,6,7,8,9,10]
  ## => ... => [45,10] => 55
  ```

  ### 2. 예제
  - 1~10까지 가진 리스트에서 각 요소의 제곱을 더하기

  ```python
  from functools import reduce

  a=list(range(1, 10+1))
  result = reduce(lambda x, y: x**2 + y**2, a)
  ```
