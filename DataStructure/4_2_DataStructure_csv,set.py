# 3. csv (comma-separated values)
# csv는 아래와 같이 표처럼 이루어져 있으며 """ or ''' 를 이용하여 다중 스트링을 저장할 수 있다.
# ============================
# 이름, 연락처, 나이, 이메일
# KS, "123-123", 12, nf@nf
# Lee, "345-345", 20, ndff@eenf
# ============================

# 예시 (split은 뒤에 설명)
csv_values = """
name, phone, age, email
KS, "123-123", 12, nf@nf
Lee, "345-345", 20, ndff@eenf
"""
print(csv_values)

# split(분해할 기준 값, 최대로 분해할 개수) : 기준값 양옆의 값을 list로 가져옴
phone = "010-1234-5678"
print(phone.split("-",1)) # 결과 : ['010', '1234-5678']
# strip(지울 값) : String 양 끝에 지정한 값이 있으면 삭제 (계속 있으면 이를 삭제)
string = "----Py-thon!!!----"
print(string.strip("-").strip("!")) # 결과 : Py-thon!!!


# csv 를 dictionary로 변환

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


# 4. Set
# 중복된 값없이 {} 로 저장
# set 만드는법
set1 = {1,2,3,4,5,4,4,4,4,5}
print(set1)


# set() : 비어있는 set을 생성 ({}를 사용할 경우 dictionary가 생성)
set2 = set()
# set.add(값) : set에 값을 추가
set2.add(1)
set2.add(7)
set2.add(7)
print(set2)

# union() : 두 set의 합집합을 가져옴
print(set1.union(set2))
# difference() : 두 set에서 비교값의 리스트에서 없는 값만 가져옴
print(set1.difference(set2))
print(set2.difference(set1))


# 4. List Comprehensions
# 리스트 안에서 for문 등을 작성하여 코드량을 줄일 수 있다.

# 예시 1 (1~20 중 2의 배수의 제곱 출력)
## === 이전
# a = []
# for i in range(1,21):
#     if i % 2 ==0:
#         a.append(i)
## === list comprehension 사용
a = [i**2 for i in range(1, 21) if i%2 == 0]
print(a)

# 예시 2 ( "[[1,2], [1,2], [1,2]]" 출력 )
##===== 이전
# listcom_ex2 = []
# for i in range(3):
#     temp2 =[]
#     for j in range(1,3):
#         temp2.append(j)
#     listcom_ex2.append(temp2)
# print(listcom_ex2)
##==== list comprehension 사용
listcom_ex2 =[ [j for j in range(1,3)] for _ in range(3) ] # "_" 의 경우 변수를 사요하지 않는 경우 이렇게 명명하는 스타일이 있다.
print(listcom_ex2)

