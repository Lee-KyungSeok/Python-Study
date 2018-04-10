# lambda

# 람다를 변수에 넣을 수도 있다.
a = lambda x, y : x + y
print(a(5, 8))  # 출력 : 13

# 람다에 바로 값을 넣어서 실행 가능
print((lambda x, y : x + y)(10, 20)) # 출력 : 30

## 예제 1
print('+1 해주는 함수 :', (lambda x: x+1)(5))
print('3개의 값을 더해주는 함수 :', (lambda x, y, z: x+y+z)(1,2,3))
print('2개의 값을 각각 제곱해서 더해주느 함수 :', (lambda x, y: x**2 + y**2)(3,4))

## 예제 2
print("1개의 숫자를 받아서 2의 배수이면 True, 아니면 False :", (lambda x : True if x%2==0 else False)(1));
print("0~n개의 정수를 받아서 다 합쳐주는 함수", (lambda *args: sum(args))(1,2,3,4))