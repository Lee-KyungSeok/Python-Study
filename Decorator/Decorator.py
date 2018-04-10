from time import time # 뒤의 예제에서 사용

def print_a_to_b(a, b, c):
    for i in range(a, b, c):
        if i<b:
            print(i, end=', ')
        else:
            print(i)

# 함수를 인자로 받는 함수를 정의
def print_start_end(func):
    print("함수가 시작됩니다.")
    result = func(1, 100, 3)
    print("함수가 끝났습니다")
    return result

print_start_end(print_a_to_b)

# 함수를 리턴하는 함수를 정의
def make_print_start_end(func):
    def new_func(a, b, c):
        print("함수가 시작됩니다.")
        result = func(a, b, c)
        print("함수가 끝났습니다")
        return result
    return new_func
newFunc = make_print_start_end(print_a_to_b)
newFunc(5, 20, 6)

# 아래처럼 packing과 unpacking 사용 가능
def make_print_start_end_p(func):
    def new_func(*args, **kwargs):
        print("함수가 시작됩니다.")
        result = func(*args, **kwargs)
        print("함수가 끝났습니다")
        return result
    return new_func


## @decorator 사용
@make_print_start_end_p
def print_a_to_b_d(a,b,c):
    for i in range(a,b,c):
        if i< b:
            print(i, end=', ')
        else:
            print(i)

print_a_to_b_d(1, 100, 2) 

## 이것과 동일하게 작동
# newFunc = make_print_start_end_p(print_a_to_b)
# newFunc(5, 20, 6)

# 예제
## 실행시간을 측정하는 데코레이터 만들기 (모듈 사용)
def make_check_time(func):
    def new_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print('실행시간 :', end_time-start_time)
        return result
    return new_func

@make_check_time
def sum_1_to_n(n):
    result = 0
    for i in range(1,n+1):
        result +=i
    return result

print(sum_1_to_n(100000))

@make_check_time
def gauss_sum(n):
    return (n*(n+1))/2
print(gauss_sum(100000))