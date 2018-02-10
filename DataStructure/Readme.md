# DataStructure
  - tuple
  - dictionary
  - csv
  - set
  - List Comprehensions
  - [몇가지 문제](https://github.com/Lee-KyungSeok/Python-Study/tree/master/DataStructure/Example)

---

## tuple
  ### 1. tuple
  - tuple은 immutable한 객체
  - tuple을 통하여 key값과 value값을 저장할 수 있다.
  - 동시에 변수 할당 가능
  - ()를 이용하여 변수 할당 혹은 tupe() 메소드 이용
  - 주의 : "a = 100, "과 같이 변수를 지정하지 않도록 주의

  ```Python
  tuple1 = (1,2,3,4,5)
  a, b = 3, 4
  print(a, b) # 출력 : 3 4
  (c, d) = (5, 6)
  print(c, d) # 출력 : 5 6
  a = 100,
  print(a) # 출력 : (100,) => 쉼표를 포함하면 tuple로 지정하게 된다.
  ```

  ### 2. 사용 예시

  > 예제 1 (range, tuple, list 활용)

  ```Python
  tuple_1_to_100 = tuple(range(1,101))
  print(tuple_1_to_100) # 출력 : (1,2,3 ..., 100)

  list_1_to_100 = list(tuple_1_to_100)
  print(list_1_to_100) # 출력 : [1,2,3 ..., 100]
  ```

  > 예제 2 (key값과 value 값을 저장)

  ```Python
  # list와 tuple을 활용 하여 key값과 value 값을 저장할 수 있다.
  my_info = [("name", "KS"), ("email","qwer1234@python.com"), ("phone","010-1234-5678"),("nation","korea")]
  for el in my_info:
      print(el[0], end=" : ")
      print(el[1])

  # 출력
  # name : KS
  # email : qwer1234@python.com
  # phone : 010-1234-5678
  # nation : korea
  ```

---

## dictionary
  ### 1. dictionary
  - key value값을 저장할 수 있으며 mutable 하기 때문에 값 수정 가능
  - dictionary를 범위에 넣을 경우 key값이 출력
  - ※ key value를 입력한 순서로 값이 저장되지 않으므로 주의할 것.
  - 사용방법
    - "중괄호 {}" 안에 key value 값을 지정하여 json 형식과 비슷하게 저장 ("," 주의 할 것)
    - 그 후에 dic[key] 와 같이 사용하여 value를 출력

  ```Python
  dictionary_1 = {
      "name" : "Lee",
      "phone" : "010-9876-5432",
      "nation" : "USA"
  }

  # key value를 추 가능(mutable)
  dictionary_1["email"] = "qwer1234@python.com"
  for el in dictionary_1:
      print(el, end=" : ")
      print(dictionary_1[el])
  ```

  ### 2. 몇가지 Api
  - get() : dicationary 이용시 key가 없을 경우 에러를 방지하기 위해 이용.
  - values() : value들을 tuple의 형태로 가져온다.
  - items() : key와 value를 tuple의 형태로 가져온다.
  - dict() : key value 형태의 tuple을 dictionary 형태로 변환

  > get()

  ```Python
  print(dictionary_1.get("nation")) # USA
  print(dictionary_1.get("city")) # None 출력

  # 활용방안 (ex> city라는 변수를 출력?)
  city = dictionary_1.get("city")
  if city:
      # city는 none이므로 False로 인식되어 이 코드가 실행되지 않는다.
      print("나는 {} 도시에 살고 있어요".format(city))
  ```

  > values()

  ```Python
  print(dictionary_1.values()) # 출력 : dict_values(['Lee', '010-9876-5432', 'USA', 'qwer1234@python.com'])

  for el in dictionary_1.values():
      print(el)
  # 출력
  # Lee
  # 010-9876-5432
  # USA
  # qwer1234@python.com
  ```

  > items()

  ```Python
  print(dictionary_1.items()) # 출력 : dict_items([('name', 'Lee'), ('phone', '010-9876-5432'), ('nation', 'USA'), ('email', 'qwer1234@python.com')])

  for el in dictionary_1.items():
      print(el)
  # 출력
  # ('name', 'Lee')
  # ('phone', '010-9876-5432')
  # ('nation', 'USA')
  # ('email', 'qwer1234@python.com')

  for key, value in dictionary_1.items():
      print(key , end=" : ")
      print(value)
  # 출력
  # name : Lee
  # phone : 010-9876-5432
  # nation : USA
  # email : qwer1234@python.com
  ```

  > dict()

  ```Python
  my_info = [("name", "KS"), ("email","qwer1234@python.com"), ("phone","010-1234-5678"),("nation","korea")]
  print(dict(my_info)) # 출력 : {'name': 'KS', 'email': 'qwer1234@python.com', 'phone': '010-1234-5678', 'nation': 'korea'}
  ```

---

## csv (comma-separated values)
  ### 1. csv
  - csv는 표처럼 이루어져 있으며 """ or ''' 를 이용하여 다중 스트링을 저장할 수 있다.

  ```Python
  csv_values = """
  name, phone, age, email
  KS, "123-123", 12, nf@nf
  Lee, "345-345", 20, ndff@eenf
  """
  print(csv_values)
  # 출력
  #
  # name, phone, age, email
  # KS, "123-123", 12, nf@nf
  # Lee, "345-345", 20, ndff@eenf
  #
  ```

  ### 2. csv 를 dictionary로 변환
  - new line과 row를 분류
  - key를 list로 저장
  - 결과 list를 선언하고 key값에 대한 인덱싱 변수 선언

  ```Python
  csv_values = csv_values.strip("\n") # 처음과 끝의 new line 을 제거
  csv_list = csv_values.split("\n") # 값을 row를 별로 분류하여 리스트로 저장

  keys = [] # key를 list로 저장
  for el in csv_list[0].split(","): # 첫번째 row를 "," 로 분해하여 key로 저장
      keys.append(el.strip(' ')) # "," 뒤에 space가 있으므로 이를 제거

  results = [] # 결과 list 선언
  for val in csv_list[1:]:
      result_dict = {} # dictionary 선언
      i = 0 # key값에 대한 인덱싱 변수 선언
      for el in val.split(","):
          result_dict[keys[i]] = el.strip(" ")
          i += 1
      results.append(result_dict) # 결과 list에 dicationary를 추가
  print(results)

  # 출력
  # [{'name': 'KS', 'phone': '"123-123"', 'age': '12', 'email': 'nf@nf'}, {'name': 'Lee', 'phone': '"345-345"', 'age': '20', 'email': 'ndff@eenf'}]
  ```

---

## set
  ### 1. set
  - 중복된 값없이 {} 로 저장
  - 비어있는 set의 경우 set()을 이용
  - 값을 추가할 경우 add() 이용

  ```Python
  set1 = {1,2,3,4,5,4,4,4,4,5}
  print(set1) # 출력 : {1, 2, 3, 4, 5}

  set2 = set()
  # set.add(값) : set에 값을 추가
  set2.add(1)
  set2.add(7)
  set2.add(7)
  print(set2) # 출력 : {1, 7}
  ```

  ### 2. union(), difference()
  - union() : 두 set의 합집합을 가져옴
  - difference() : 두 set에서 비교값의 리스트에서 없는 값만 가져옴

  ```Python
  print(set1.union(set2)) # 출력 : {1, 2, 3, 4, 5, 7}

  print(set1.difference(set2)) # 출력 : {2, 3, 4, 5}
  print(set2.difference(set1)) # 출력 : {7}
  ```

---

## List Comprehensions
  ### 1. List Comprehensions
  - 리스트 안에서 for문 등을 작성하여 코드량을 줄일 수 있다.

  > 예시 1 (1~20 중 2의 배수의 제곱 출력)

  ```Python
  ## === 이전
  a = []
  for i in range(1,21):
      if i % 2 ==0:
          a.append(i)

  ## === list comprehension 사용
  a = [i**2 for i in range(1, 21) if i%2 == 0]
  print(a)

  # 출력 : [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
  ```

  > 예시 2 ( "[[1,2], [1,2], [1,2]]" 출력 )

  ```Python
  ## ==== 이전
  listcom_ex2 = []
  for i in range(3):
      temp2 =[]
      for j in range(1,3):
          temp2.append(j)
      listcom_ex2.append(temp2)
  print(listcom_ex2)

  ## ==== list comprehension 사용
  listcom_ex2 =[ [j for j in range(1,3)] for _ in range(3) ]
  # "_" 의 경우 변수를 사용하지 않는 경우 이렇게 명명하는 스타일이 있다.
  ```

---
