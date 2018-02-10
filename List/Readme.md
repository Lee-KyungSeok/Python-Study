# List
  - list 구성
  - list 관련 함수 및 Api

---

## list 기본
  ### 1. list 기본
  - list는 "[ ]" 를 통해 만들며, indexing과 sliceing 이 가능
  - 리스트의 경우 원하는 값으로 변경 가능 (mutable)
  - 리스트는 모든 값들이 객체로 저장되며 리스트의 주소값을 가지고 있다.

  ```Python
  list_ex = [1, 2.3, "String", 2, 3] # list 만들기
  print(list_ex[0], list_ex[-1], list_ex[1:-1], list_ex[::2]) #인덱싱 및 슬라이싱

  list_ex[4] = 50 # 원하는 값으로 변경 가능
  ```

  ### 2. list()
  - 리스트를 만들 수 있다.

  ```Python
  listEx1 = list("python")
  print(listEx1) # 출력 : ['p', 'y', 't', 'h', 'o', 'n']
  listEx2 = list(range(30)) # range는 0~29를 포함.. 반복문 설명시 나옴
  ```

  ### 3. 참고사항
  - 리스트는 주소값을 가지게 되므로 리스트를 복사할 때 주의할 것 (이 때 copy() 라는 메소드를 이용)

  ```Python
  a = [1,2,3]
  b = a
  b.append(4)
  print(a) # a에도 4가 추가되게 된다.
  ```

---

## list 함수 및 Api
  ### 1. append()
  - 변수를 추가한다.

  ```Python
  likes2 = ["치킨"]
  likes2.append("고양이")
  likes2.append("씨리얼")
  ```

  ### 2. del
  - 변수를 제거한다.
  - del 함수는 리스트를 인덱싱 및 슬라이싱 한 것을 삭제가능

  ```Python
  listEX = [1,2,3,4,5,6,7,8,9]
  del listEX[0]
  del listEX[1::2]
  ```

  ### 3. reverse()
  - 리스트 내용 순서를 뒤집는다.

  ```Python
  likes2 = ["치킨", "고양이", "씨리얼"]
  likes2.reverse()
  print(likes2) # 출력 : ["씨리얼", "고양이", "치킨"]
  ```

  ### 4. sort()
  - 리스트를 정렬한다.

  ```Python
  numbers = [1,34,65,2,3,5,2,7]
  numbers.sort()
  print(numbers) # 출력 : [1,2,2,3,5,7,34,65]
  ```

  ### 5. pop()
  - 특정 인덱스의 값을 튕겨낸다
  - del 함수와는 다르게 튕겨낸 값을 리턴한다.

  ```Python
  numbers = [1,34,65,2,3,5,2,7]
  numbers.pop(4)
  print(numbers) # 출력 : [1,34,65,2,5,2,7]

  # <del과 차이점>
  # numbers = [1,2,3,4,5,6,7,8]
  # print(numbers.pop(0)) => 출력값 : 2
  # numbers = [1,2,3,4,5,6,7,8]
  # print(del numbers[0]) => 출력 에러
  # 따라서 지워진 넘버를 알아 할 때 유용
  ```

  ### 6. insert(index, object)
  - 특정 인덱스에 값을 넣는다.

  ```Python
  numbers = [1,2,3,4,5,6,7,8]
  numbers.insert(0,11)
  print(numbers) # 출력 : [11, 1, 2, 3, 4, 5, 6, 7, 8]
  ```

  ### 7. extend(list)
  - 리스트를 더해주면서 값에 저장

  ```Python
  numbers = [11,1,2,3,4,5,6,7,8]
  numbers2 = [9,10,11,12]
  numbers.extend(numbers2)
  print(numbers) # 출력 : [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  ```

  ### 8. count()
  - 특정값과 동일한 값이 몇개 있는지 출력

  ```Python
  numbers = [1,1,3,1,5,4,3,3]
  print(numbers.count(1)) # 출력 : 3
  ```  

  ### 9. remove()
  - 가장 먼저 나온 특정값을 제거

  ```Python
  numbers = [1,3,1,2,3,4,5,6,7,8]
  numbers.remove(3)
  print(numbers) # 출력 : [1, 1, 2, 3, 4, 5, 6, 7, 8]
  ```  

  ### 10. copy()
  - 값을 복사하되 새로운 주소값을 지정하여 분배한다.

  ```Python
  a=[1,2,3,4,5]
  b=a.copy()
  b.append(6)
  print(a) # a는 6이 추가되지 않는다.
  ```  

  ### 11. sum(list)
  - 리스트의 숫자들을 더한다

  ```Python
  numbers = range(1,21)
  print(sum(numbers)) # 출력 : 210
  ```
