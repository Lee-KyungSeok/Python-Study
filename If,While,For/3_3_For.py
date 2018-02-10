# for

#for 변수 in 리스트 / range(숫자)
#   실행코드

#예시(리스트)
for el in [1, 2, 3, 4]:
    print(el)
for c in "python":
    print(c)

#예시(range => 1부터 10까지 출력) # range는 list가 아니다
for i in range(1, 10+1):
    print(i)

# 직접해보기 (1~10 까지 더한값 출력)
result = 0
for i in range(1,11):
    result += i
print(result)

# list() : 리스트를 만든다
print(list("python"))
listEx = list(range(30)) # 0~29까지를 리스트로 만든다
print(listEx)

# pass : 건너 뛴다
for i in range(1,10):
    if i % 2 == 0:
        print("{}짝수입니다.".format(i))
    else:
        pass # 작동하지 않지만 pass 하여 지나치게 된다

# sum : 리스트를 더한다.
numbers = range(1,21)
print(sum(numbers))

# 2와 3의 약수 더하기
num = 0
for i in range(1,10):
    if i<=3:
        if 3%i == 0:
            num += i
        elif 2%i == 0:
            num += i
        else:
            pass
print(num)

# 3, 5, 15의 배수에 따라 다르게 출력
for index in range(1,20):
    if index %3 ==0 and index %5 != 0:
        print("fizz")
    elif index %3 !=0 and index %5 == 0:
        print("buzz")
    elif index %3 ==0 and index %5 == 0:
        print("fizzbuzz")
    else:
        print(index)

# 1~ 1000 중 소수 판별 (1)
for i in range(1,1001):
    if i==1 or i==2:
        print("{}는 소수입니다.".format(i))
    else:
        value = 0
        for j in range(2, i):
            if i % j ==0:
                value = 1
                break
        if value == 0:
            print("{}는 소수입니다.".format(i))
                 
