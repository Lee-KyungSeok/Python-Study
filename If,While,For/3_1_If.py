# 모듈 불러오기 (import 함수)
import random #random 모듈을 사용

# if
# <사용방법 : ":"을 붙이고 탭만큼 들여써준다.
#if bool:
#   실행코드(ex> print("bool is True") )
#elif bool2"
#   실행코드
#else:
#   실행코드

## 예시1
if 3 < 5:
    print("3은 5보다 작습니다.")
    #if문은 여기까지 들여쓰기 된 부분까지
print("여기는 항상 실행된다.") # 들여쓰기가 되지 않으면 항상 실행

## 예시2 (if, else)
if 'p' in "python":
    # 참인 경우 실행
    print("p라는 글자는 python 안에 포함되어 있습니다.")
else:
    # 거짓인 경우 실행
    print("p는 python 안에 포함되어 있지 않습니다.")

## 예시3(elif 및 다중조건)
num = int(input("0~9까지 숫자를 하나 입력하세요")) # 그냥 input으로 할 경우 String 형식으로 받기 때문에 int로 변환
if num > 8:
    print("입력한 값이 8보다 큽니다.")
elif num > 5:
    print("입력한 값이 8보다 작거나 같고, 5보다 큽니다.")
else:
    if num > 2:
        print("입력한 값이 5보다 같거나 작고, 2보다는 큽니다. ")
    else:
        print("입력한 값이 2보다 작거나 같습니다.")

## 직접해보기
num = float(input("1 ~ 10까지 숫자 중 실수를 입력"))
if num < 3:
    print("3보다 작아요")
elif num <6:
    print("3과 같거나 크고 6보다 작네요")
else:
    print("6과 같거나 보다 크네요!")

#and : 둘다 True인 경우 True를 반환
#or : 둘중 하나만 True인 경우 True를 반환

#random
n = random.randint(1,10)
print(n)
#abs()
print(abs(10-15)) # 둘의 차이(절댓값을 불러옴)

# 직접해보기 (1~100 랜덤으로 뽑아 입력한 값과 차이를 비교)
n = random.randint(1,100)
guess = int(input("1~100 사이 입력"))
if abs(n-guess)<=10 and n!=guess:
    print("아깝네요")
elif n==guess:
    print("정답")
else:
    print("틀렸습니다.")
print(n, guess)
