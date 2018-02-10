import random
# while

# <사용방법 : 조건문 후에 ":"을 붙이고 그 다음줄부터 탭만큼 들여써준다, break를 쓸 경우 빠져나오게 된다.
#if bool:
#   실행문

# 예제1 ( 1부터 5까지 출력 )
n=1
while n <= 5:
    print(n)
    n += 1
# 예제2 (break문 활용)
n=1
while True:
    print(n)
    n+=1
    if n>5:
        break

# 직접해보기 (1~100 랜덤으로 뽑아 입력한 값과 차이를 맞출때까지 비교)
n = random.randint(1,100)
while True:
    guess = int(input("100 이하의 정수값 입력"))
    if n == guess:
        print("정답입니다.")
        break
    elif abs(n-guess) <=10:
        print("아깝습니다")
    else:
        print("틀렸습니다.")
        