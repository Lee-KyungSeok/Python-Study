# File IO
  - open
  - with
  - 참고 -  Whitespace Character, pprint

---

## open
  ### 1. dd
  - dd

  ```Python

  ```

---

## with
  ### 1. dd
  - dd

  ```Python

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
