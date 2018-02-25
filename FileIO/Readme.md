# File IO
  - open
  - with
  - 참고 -  Whitespace Character, pprint

---

## open
  ### 1. 사용방법
  - `open`을 이용하기 위해서는 경로와 모드가 필요
  - 경로
    - 상대경로 : 상대적인 디렉토리 파악 (현재 디렉토리의 파일인 경우 "./" 을 경로로 지정)
    - 절대경로 : 파일의 절대 위치를 파악 (윈도우의 경우 \\\\ 두개 씩 작성해야 한다.)
  - 모드
    - `w` : write 모드, 파일 전체에 새로 쓰기, 파일이 없다면 생성
    - `r` : read 모드, 파일을 읽는 모드
    - `a` : append 모드, 파일에 내용을 추가하는 모드
  - 파일을 read 하는 경우 커서가 읽은 후를 가리키고 있으므로 `f.seek(0)` 인 0번째 글자로 커서를 옮겨 주는 메소드를 이용하여 다시 read 해야 한다.

  > 사용방법

  ```Python
  f = open("파일경로", "모드")
  # 로직작성
  f.close()
  ```

  ### 2. 예제
  - `readline` 의 경우 한줄씩 읽도록 해준다.

  > 상대경로

  ```Python
  # 상대경로 - write
  f = open("./hello.txt","w")
  f.write("Hello World!")
  f.close() # hello.txt을 만들고 여기에 "Hello World!" 내용을 저장

  # 상대경로 - append
  f = open("./hello.txt", "a")
  for i in range(2, 10+1):
      content ="\n" + str(i) + "번째 줄입니다."
      f.write(content)
  f.close()  # hello.txt 파일에 작성한 내용들을 추가

  # 상대경로 - read
  f = open("./hello.txt", "r")
  content = f.read()
  print(content)
  f.seek(0) # 이는 0번째 글자로 커서를 옮겨 주는 메소드로 다시 read 할 수 있게 된다.
  f.close()  # hello.txt 파일에 저장된 내용을 읽는다.
  ```

  > 절대경로

  ```Python

  # 절대경로 - read
  f2 = open("C:\\workspaces\\Python\\FileIO\\hello.txt", "r")
  content2 = f2.read()
  print(content2)
  f2.close()

  # 절대경로 - readline
  f = open("C:\\workspaces\\Python\\FileIO\\hello.txt", "r")
  print(f.readline())
  print(f.readline())
  f.close()
  ```

---

## with
  ### 1. 개념 및 사용방법
  - `with` 는 자동으로 닫아주는 기능을 수행 (즉, close를 자동으로 실행해준다)
  - 이는 enter와 exit 이라는 메소드를 실행하는 기능을 한다.

  ```Python
  with open("path", "mode") as f:
  #   로직 작성 (ex> f.write)
  ```

  ### 2. 예제
  - `f.closed` 의 경우 잘 파일이 닫혀있는지 확인하는 기능을 수행한다.

  ```Python
  with open("./new.txt", "w") as f:
      f.write("안녕하세요! with입니다.")

  if not f.closed:
      print("파일을 꺼야합니다")
  else:
      print("파일이 꺼져있습니다.")
  ```
---

## 참고
  ### 1. Whitespace Character
  - \\n : 새로운 줄을 만들 때
  - \\t : 탭만큼 공간을 만들 때
  - 이 때문에 윈도우에서는 \\\\ 을 두번써줘야 경로 지정이 가능하다.

  ```Python
  print("Hello \n my name is python")
  # 출력 : Hello
  #        my name is python

  print("Hello \t my name is python")
  # 출력 : Hello   my name is python
  ```

  ### 2. pprint
  - 리스트나, 딕셔너리를 알아보기 쉽게 출력해준다.
  - import 한 후 pprint.pprint("값") 으로 출력한다.

  > 예시 (print 와 pprint 비교)

  ```Python
  import pprint
  list_info = [
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
  ]
  print(list_info)
  pprint.pprint(list_info)
  ```

  > 결과

  ```
  # print
  [{'전화번호': '010-1234-5678', '이름': '지코', '나이': '24'}, {'전화번호': '010-1234-2334', '이름': '도끼', '나이': '27'}, {'전화번호': '010-9234-6382', '이름': '해지', '나이': '26'}]

  # pprint
  [{'나이': '24', '이름': '지코', '전화번호': '010-1234-5678'},
   {'나이': '27', '이름': '도끼', '전화번호': '010-1234-2334'},
   {'나이': '26', '이름': '해지', '전화번호': '010-9234-6382'}]
  ```
