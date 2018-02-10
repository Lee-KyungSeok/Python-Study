# 조건문(if), 반복문(while, for)
  - if
  - while
  - for
  - 모듈 불러오기, pass, all, any, range
  - [몇가지 문제(Palindrome)](https://github.com/Lee-KyungSeok/Python-Study/tree/master/If%2CWhile%2CFor/Example)

---

## if
  ### 1. 사용방법
  -  ":"을 붙이고 탭만큼 들여써준다.
  - if / elif / else 로 조건문을 순서대로 진행시킬 수 있다.
  - 다중조건을 이용할 경우 한칸 더 탭을 한 뒤 사용한다.

  ```Python
  #if bool:
  #   실행코드(ex> print("bool is True") )
  #elif bool2"
  #   실행코드
  #else:
  #   실행코드
  ```

  ### 2. 사용 예시

  ```Python
  # 예시 1
  if 3 < 5:
      print("3은 5보다 작습니다.")
      #if문은 여기까지 들여쓰기 된 부분까지
  print("여기는 항상 실행된다.") # 들여쓰기가 되지 않으면 항상 실행

  # 예시 2 (if, else)
  if 'p' in "python":
      # 참인 경우 실행
      print("p라는 글자는 python 안에 포함되어 있습니다.")
  else:
      # 거짓인 경우 실행
      print("p는 python 안에 포함되어 있지 않습니다.")

  # 예시 3(elif 및 다중조건)
  num = int(input("0~9까지 숫자를 하나 입력하세요"))
  if num > 8:
      print("입력한 값이 8보다 큽니다.")
  elif num > 5:
      print("입력한 값이 8보다 작거나 같고, 5보다 큽니다.")
  else:
      if num > 2:
          print("입력한 값이 5보다 같거나 작고, 2보다는 큽니다. ")
      else:
          print("입력한 값이 2보다 작거나 같습니다.")

  # 예시 4
  n = random.randint(1,100)
  guess = int(input("1~100 사이 입력"))
  if abs(n-guess)<=10 and n!=guess:
      print("아깝네요")
  elif n==guess:
      print("정답")
  else:
      print("틀렸습니다.")
  print(n, guess)

  ```

---

## while
  ### 1. 사용방법
  - 조건문 후에 ":"을 붙이고 그 다음줄부터 탭만큼 들여써준다
  - break를 쓸 경우 빠져나오게 된다.

  ```Python
  #if bool:
  #   실행문
  ```

  ### 2. 사용 예시

  ```Python
  # 예제 1 ( 1부터 5까지 출력 )
  n=1
  while n <= 5:
      print(n)
      n += 1

  # 예제 2 (break문 활용)
  n=1
  while True:
      print(n)
      n+=1
      if n>5:
          break

  # 예제 3 (1~100 랜덤으로 뽑아 입력한 값과 차이를 맞출때까지 비교)
  n = random.randint(1,100)
  while True:
      guess = int(input("100 이하의 정수값 입력"))
      if n == guess:
          print("정답입니다.")
          break
      elif abs(n-guess) <=10:
          print("아깝습니다")
      else:
          print("틀렸습니다.")
  ```

---

## for
  ### 1. 사용방법
  - for문에 "in" 을 쓰고 리스트 혹은 range를 넣는다.

  ```Python
  #for 변수 in 리스트 / range(숫자)
  #   실행코드
  ```

  ### 2. 사용 예시

  ```Python
  # 예시 1 (리스트)
  for el in [1, 2, 3, 4]:
      print(el)
  for c in "python":
      print(c)

  # 예시 2 (range => 1부터 10까지 출력)
  for i in range(1, 10+1):
      print(i)

  # 예시 3 (2와 3의 약수 더하기)
  num = 0
  for i in range(1,10):
      if i<=3:
          if 3%i == 0:
              num += i
          elif 2%i == 0:
              num += i
          else:
              pass
  print(num)

  # 예시 4 (3, 5, 15의 배수에 따라 다르게 출력)
  for index in range(1,20):
      if index %3 ==0 and index %5 != 0:
          print("fizz")
      elif index %3 !=0 and index %5 == 0:
          print("buzz")
      elif index %3 ==0 and index %5 == 0:
          print("fizzbuzz")
      else:
          print(index)

  # 예시 5 (1~ 1000 중 소수 판별)
  for i in range(1,1001):
      if i==1 or i==2:
          print("{}는 소수입니다.".format(i))
      else:
          value = 0
          for j in range(2, i):
              if i % j ==0:
                  value = 1
                  break
          if value == 0:
              print("{}는 소수입니다.".format(i))
  ```
---

## 참고사항
  ### 1. 모듈 불러오기
  - import 함수를 통해 모듈을 불러올 수 있다.

  ```Python
  import random # random 모듈을 사용
  ```

  ### 2. range(start, stop, step=1)
  - for문 등을 이용할 때 범위를 지정할 수 있다.
  - start : 시작, stop : 끝, step : 건너뛸 step 수
  - start가 시작 stop의 전까지 실행된다.
    - ex1> range(0, 10) : 0 ~ 9 까지 실행
    - ex2> range(1, 11) : 1 ~ 10 까지 실행

  ```Python
  # 예시 1
  for i in range(1,10): # 1,10 까지면 1~9 까지 실행됨
      if i % 2 == 0:
          print("{}짝수입니다.".format(i))

  # 예시 2
  listEx = list(range(30)) # start 범위가 없으면 0~29
  ```

  ### 3. pass
  - 조건문 및 반복문을 건너뛸 수 있다.

  ```Python
  for i in range(1,10):
      if i % 2 == 0:
          print("{}짝수입니다.".format(i))
      else:
          pass # 작동하지 않지만 pass 하여 지나치게 된다
  ```

  ### 4. all 과 any
  - 리스트의 조건에 따라 True 및 False를 반환

  ```Python
  print(any([False, False, False])) #False 반환
  print(any([False, True, False])) #True 반환

  print(all([False, False, False])) #False 반환
  print(all([False, True, False])) #False 반환
  print(all([True, True, True])) #True 반환
  ```
