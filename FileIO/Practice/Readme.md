# File IO 문제 예시
  - 1. Hello World 10번, Hello Python 10번 입력하고 각각 20번 10번 읽기
  - 2. csv 파일 변환 예제

---

## Hello World 10번, Hello Python 10번 입력하고 각각 20번 10번 읽기
  - open을 사용하는 경우
  - with를 사용하는 경우

  ```Python
  def writeFile(path, text):
      f = open(path, "w")
      f.write(text)
      f.close()

  def appendFile(path, text):
      f = open(path, "a")
      f.write(text)
      f.close()

  content = ""
  for _ in range(10):
      content += "hello world!\n"
  writeFile("./sample.txt", content)

  for _ in range(10):
      appendFile("./sample.txt","hello python!\n")

  for i in range(11):
      f = open("./sample.txt","r")
      if(i<10):
          content = f.readline()
          print(content, end="")
      else:
          f.seek(0)
          print(f.read())
          f.close()

  # with를 쓴다면
  with open("./sample.txt","r") as f:
      for _ in range(10):
          print(f.readline(), end="")
  with open("./sample.txt","r") as f:
      print(f.read())
  ```

---

## csv 파일 변환 예제
  - key값이 최소 3개 이상인 dictionary를 최소 3개 포함한 리스트를 csv파일로 만들어서 저장하는 함수 만들기
  -  저장한 csv 파일을 불러와서 다시 dictionary로 변환하는 함수 만들기

  > 0. import 및 dictionary 만들기

  ```Python
  # 파일을 지정 + pprint import
  import pprint
  FILE = "./info.txt"

  # dictionary 만들기
  dic_info1 = {
      "전화번호" : "010-1234-5678",
      "이름" : "지코",
      "나이" : "24"
  }
  dic_info2 = {
      "전화번호" : "010-1234-2334",
      "이름" : "도끼",
      "나이" : "27"
  }
  dic_info3 = {
      "전화번호" : "010-9234-6382",
      "이름" : "해지",
      "나이" : "26"
  }
  list_info = []
  list_info.append(dic_info1)
  list_info.append(dic_info2)
  list_info.append(dic_info3)
  ```

  > 1. csv 파일로 저장

  ```Python
  def make_csv(listValue, filename):
      long_str = ""

      # key값 넣기
      keys = []
      for i in listValue[0]:
          keys.append(i)
      long_str += ", ".join(keys) + "\n"

      # value 값 넣기
      for dic in listValue:
          value = []
          for v in dic.values():
              value.append(v)
          long_str += ", ".join(value) + "\n"

      # 파일 저장하기
      f = open(filename,"w")
      f.write(long_str)
      f.close  

  make_csv(list_info, FILE)
  ```

  > 2. csv 파일 불러와서 dictionary로 저장

  ```Python
  def csv_to_dictionary(filename):
      # 파일 불러오기
      with open(filename, "r") as f:
          csv_value = f.read()

      # 문자 자르기
      csv_value = csv_value.strip("\n")
      csv_list = csv_value.split("\n")

      # key 값 넣기
      keys = []
      for key_el in csv_list[0].split(","):
          keys.append(key_el.strip(' '))

      # vlaue 값 넣기
      values = []
      for value_mem in csv_list[1:]:
          info_value = []
          for v in value_mem.split(","):
              info_value.append(v.strip(" "))
          values.append(info_value)

      # dictionary로 바꾸기
      dic_list = []
      for gr in values:
          dic_info = {}
          i = 0
          for el in keys:
              dic_info[keys[i]] = gr[i]
              i += 1
          dic_list.append(dic_info)

      return dic_list

  pprint.pprint(csv_to_dictionary(FILE))
  ```
