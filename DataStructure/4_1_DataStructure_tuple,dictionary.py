# 1. Tuple
# tuple은 immutable한 객체 (list는 mutable한 객체)
# ※ tuple을 1부터 100까지 만들기 위해서는 직접 전부 입력해주어야 한다.
# tutpe() 함수를 사용하여 생성 가능
# <사용법> ()를 이용
tuple1 = (1,2,3,4,5)

# 동시에 변수 할당 가능, tuple로 만들어도 할당 가능
# 주의 : "a = 100, "과 같이 변수를 지정하지 않도록 주의
a, b = 3, 4
print(a, b)
(c, d) = (5, 6)
print(c, d)
a = 100,
print(a)

# 예제 (range, tuple, list 활용)
tuple_1_to_100 = tuple(range(1,101))
print(tuple_1_to_100)
list_1_to_100 = list(tuple_1_to_100)
print(list_1_to_100)

# list와 tuple을 활용 하여 key값과 value 값을 저장할 수 있다.
my_info = [("name", "KS"), ("email","qwer1234@python.com"), ("phone","010-1234-5678"),("nation","korea")]
for el in my_info:
    print(el[0], end=" : ")
    print(el[1])

# 2. Dictionary
# key value값을 저장할 수 있으며 mutable 하기 때문에 값을 수정할 수 있다.
# ※ key value를 입력한 순서로 값이 저장되지 않으므로 주의할 것.
# <사용방법> "중괄호 {}" 안에 key value 값을 지정하여 json 형식과 비슷하게 저장 ("," 주의 할 것)
#           그 후에 dic[key] 와 같이 사용하여 value를 출력
# 예시
dictionary_1 = {
    "name" : "Lee",
    "phone" : "010-9876-5432",
    "nation" : "USA"
}
dictionary_1["email"] = "qwer1234@python.com" # key value를 추가할 수 있음(mutable 함)
for el in dictionary_1:
    print(el, end=" : ")
    print(dictionary_1[el])

# get() : dicationary 이용시 key가 없을 경우 에러를 방지하기 위해 이용.
print(dictionary_1.get("nation")) # USA
print(dictionary_1.get("city")) # None 출력
# 활용방안 (ex> city라는 변수를 출력?)
city = dictionary_1.get("city")
if city:
    # city는 none이므로 False로 인식되어 이 코드가 실행되지 않는다.
    print("나는 {} 도시에 살고 있어요".format(city))

# values() : value들을 tuple의 형태로 가져온다.
print(dictionary_1.values()) 
for el in dictionary_1.values():
    print(el)
# items() : key와 value를 tuple의 형태로 가져온다.
print(dictionary_1.items())
for el in dictionary_1.items():
    print(el)
for key, value in dictionary_1.items():
    print(key , end=" : ")
    print(value)

# dict() : key value 형태의 tuple을 dictionary 형태로 변환
my_info = [("name", "KS"), ("email","qwer1234@python.com"), ("phone","010-1234-5678"),("nation","korea")]
print(dict(my_info))