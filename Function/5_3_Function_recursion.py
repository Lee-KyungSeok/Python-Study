# 6. Recursion Function
# 함수 안에서 자신의 함수를 호출

# 예시 1 (factorial)
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5)) # 출력 : 120

# 예시 2 (a와 n을 더하는 함수)
def add_n(a,n):
    if n==0:
        return a
    return 1 + add_n(a,n-1)
print(add_n(10, 5)) # 출력 : 15

# 7. 예외처리
# 예외처리를 사용할 시 반드시 어떤 에러인지 지정하도록 한다.
# TypeError(string+int 등), NameError(선언한적 없는 변수 사용), ZeroDivisionError(0으로 나눔) 등 존재

# 사용법
# try:
#     Error 발생할 우려가 있는코드
# except:
#     Error 발생시 작동하는 코드

# 예시 1
try:
    # int형이고 0이 아닌경우 경우 여기서 실행
    num = input("숫자를 입력하세요")
    num = int(num)
    print(10/num)
except ValueError: 
    # string으로 입력받게 되면 여기서 실행
    print("숫자키로 입력해주세요")
except ZeroDivisionError:
    # 0으로 입력받게 되면 여기서 실행
    print("0을 제외하고 입력해주세요")