# 4. packing

# 위치 인자를 받는 packing
## *args 로 표현 (*는 필수이며 args 는 변수 이름을 관용적으로 표현)
## 넣은 값들이 tuple 로 들어오게 된다.

# 예시 1
def print_all(*args):
    print(args)
print_all(1,2,3,4,5,6) # 출력 : (1, 2, 3, 4, 5, 6)

# 예시 2
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,5,6,7,8,9,10)) # 출력 : 55

# 키워드 인자를 받는 packing
## **kwargs 로 표현(**는 필수이며 kwargs 는 변수 이름을 관용적으로 표현)
## 넣은 값들이 dictionary 형태로 들어오게 된다.

# 예시 1
def print_f_name(**kwargs):
    print(kwargs)
print_f_name(father = "임꺽정", mother = "김말숙", sister = "둘리", brother = "존", cat = "나비")
# 출력 : {'father': '임꺽정', 'mother': '김말숙', 'sister': '둘리', 'brother': '존', 'cat': '나비'}

# 예시 2
def print_f_name2(**kwargs):
    for key in kwargs:
        print(key, '의 이름은', kwargs[key], '입니다.')
print_f_name2(father = "임꺽정", mother = "김말숙", sister = "둘리", brother = "존", cat = "나비")
# 출력
# father 의 이름은 임꺽정 입니다.
# mother 의 이름은 김말숙 입니다.
# sister 의 이름은 둘리 입니다.
# brother 의 이름은 존 입니다.
# cat 의 이름은 나비 입니다.

# 5. unpacking
# packing되어 있는 경우 이를 unpacking 하는 개념
# 함수 호출 할 때 * 혹은 **을 붙여 사용한다.

# 예시 1
def print_all_un(*args):
    print(args)
print_all_un([1,2,3,4,5,6,7,8,9,10]) # 출력 : ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],)
print_all_un(*[1,2,3,4,5,6,7,8,9,10]) # 출력 : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 예시 2
def sum_all_un(*args):
    return sum(args)
# print(sum_all_un([1,2,3,4,5,6,7,8,9,10])) # 출력 : 오류
print(sum_all_un(*[1,2,3,4,5,6,7,8,9,10])) # 출력 : 55

# 예시 3 (keyword 존재)
family_dict = {
    "father" : "임꺽정", 
    "mother" : "김말숙", 
    "sister" : "둘리", 
    "brother" : "존", 
    "cat" : "나비"
}
def print_f_name_un(**kwargs):
    for key in kwargs:
        print(key, '의 이름은', kwargs[key], '입니다.')
print_f_name_un(**family_dict)
# 출력
# father 의 이름은 임꺽정 입니다.
# mother 의 이름은 김말숙 입니다.
# sister 의 이름은 둘리 입니다.
# brother 의 이름은 존 입니다.
# cat 의 이름은 나비 입니다.

# 해보기 (호출해서 입력 받고싶은 만큼 받고 최종 결과물 호출)
def input_likes():
    likes = []
    while True:
        likes_temp = input("좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력")
        if likes_temp == "exit":
            break
        else:
            likes.append(likes_temp)
    return likes
def print_likes(*args):
    print(args)
print_likes(*input_likes())

# 출력
# 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력cat
# 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력dog
# 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력whale
# 좋아하는 것을 입력하고 싶은 만큼 입력하세요 / 종료는 exit 입력exit
# ('cat', 'dog', 'whale')
            