# 데이터 구조

# list는 [] 를 통해 만들며, indexing과 sliceing 이 가능
list1 = [1, 2.3, "String", 2, 3]
print(list1[0], list1[-1], list1[1:-1], list1[::2])
# 리스트의 경우 원하는 값으로 변경 가능 (mutable 하다)
list1[4] = 50
print(list1)
# append()를 통해 변수를 넣을 수 있다.
list1.append(8)
list1.append(9)
print(list1)
# 예시1
likes2 = []
likes2.append("치킨")
likes2.append("고양이")
likes2.append("씨리얼")
print(likes2)
# del 을 통해 리스트 멤버를 지울 수 있다.
del list1[0]
print(list1)
# reverse를 통해 리스트 내용 순서를 뒤집을 수 있다.
list1.reverse()
print(list1)
# 예시2
listEX = [1,2,3,4,5,6,7,8,9]
listEX.append(10)
print(listEX[0], listEX[9:10], listEX[0:3], listEX[0:2]+listEX[-2:])
listEX.reverse()
print(listEX)
del listEX[1::2] # 혹은 listEX = listEX[::2] 를 사용
print(listEX)

# 다양한 메소드
numbers = [1,34,65,2,3,5,2,7]
# sort() : 리스트를 정렬
numbers.sort()
print(numbers)
# pop(인덱스) : 특정 인덱스의 값을 튕겨낸다
numbers.pop(4)
print(numbers)
## <del과 차이점>
## numbers = [1,2,3,4,5,6,7,8]
## print(numbers.pop(0)) => 출력값 : 2
## numbers = [1,2,3,4,5,6,7,8]
## print(del numbers[0]) => 출력 에러
## 따라서 아래와 같이 지워진 넘버를 알아 할 때 유용
numbers = [1,2,3,4,5,6,7,8]
del_num = numbers.pop(2)
print(numbers, del_num)
# insert(들어갈 인덱스, 들어갈 값) : 특정 인덱스에 값을 입력
numbers = [1,2,3,4,5,6,7,8]
numbers.insert(0,11)
print(numbers)
# extend(리스트) : 리스트를 더해주면서 값에 저장
## + 를 사용하여 지정하는 것보다 extend를 사용하는 것이 속도면에서 빠르다.
numbers2 = [9,10,11,12]
numbers.extend(numbers2)
print(numbers)
# count(값) : 특정값과 동일한 값이 몇개 있는지 출력
numbers = [1,1,3,1,5,4,3,3]
print(numbers.count(1))
# remove(값) : 가장 먼저 나온 특정값은 제거
numbers = [1,3,1,2,3,4,5,6,7,8]
numbers.remove(3)
print(numbers)

# 리스트 복사 (주의할 것)
## 리스트는 모든 값들이 객체로 저장되며 리스트의 주소값을 가지고 있다.
## 예시
a = [1,2,3]
b = a
b.append(4)
print(a) # a에도 4가 추가되게 된다.

# copy() : 값을 복사하되 새로운 주소값을 지정하여 분배한다.
a=[1,2,3,4,5]
b=a.copy()
b.append(6)
print(a) # a는 6이 추가되지 않는다.
