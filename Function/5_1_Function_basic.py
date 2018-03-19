# 추상화 : 별도에 공간에 존재하여, 변수간 간섭되는 방해를 일으키지 않는 방법
# 분리 : 코드는 다른곳에 작성되어, 우리가 필요한 경우 호출만 하여 사용할 수 있는 방법
# 이둘을 포함하는 것이 바로 "Function"

# 함수 작성 법
# def func_name(arg):
#      #코드 작성
#   print(“Hello, Func”)
#   return None

# 예시 1
def print_hello_world():
    print("hello world")
    return None
print_hello_world()

# 예시 2
def sum_3(a , b, c):
    return a + b + c
print(sum_3(1,3,5)) # 출력 : 9
print(sum_3(1,3, sum_3(4,5,6))) # 출력 : 19

# 예시 3
def add_mark(word):
    return word + "!!!!"
result_string = add_mark("python")
print(result_string) # 출력 : python!!!!

# 예시 4 (전역변수)
# 함수 안에 변수가 없다면 함수 이전에 존재하는 전역변수를 참조하게 된다.
a, b = 3, 4
def print_other(val):
    a = 1
    return val + a + b
print(print_other(5)) # 출력 : 10

# 예시 4
def number_choice():
    number = int(input("1~9까지 숫자를 입력해주세요"))
    return number
def multi_2(number):
    return number * 2
def add_5(number):
    return number + 5
def multi_50(number):
    return number * 50
def add_1769(number):
    return number + 1769
def sub_year(number):
    return number - 1993

number = number_choice()
number = multi_2(number)
number = add_5(number)
number = multi_50(number)
number = add_1769(number)
number = sub_year(number)
print(number)

# 2. default value
# 파라미터를 정의 할 때 default 값을 정의할 수 있으며 이 때 default값이 정의되어 있으면 함수에 파라미터를 넣지 않아도 에러가 발생하지 않는다.
# 주의 : default value는 항상 뒤에 와야 한다. def function(a=1, b) => 불가능
# def func_name(value, default value):

# 예시
def add(a, b=1):
    return a + b
print("a만 입력 :", add(1)) # 출력 : 2
print("a,b 둘다 입력 :", add(1,5)) # 출력 : 6

# 예시 2 (range를 받아 list로 변환하는 함수)
def range_list(start, end=None, step=None):
    if not end and not step:
        return(list(range(start)))
    elif not step:
        return(list(range(start,end)))
    else:
        return(list(range(start, end, step)))
print(range_list(10)) # 출력 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_list(1,10)) # 출력 : [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_list(1,10,2)) # 출력 : [1, 3, 5, 7, 9]

# 3. def func_name(위치인자, 키워드인자):
# 위치에 따라 출력될 수 있지만 파라미터의 키워드를 함께 입력해서 다른 위치에서도 넣을 수 있다.
# 주의 : 위치인자는 항상 키워드인자 앞에 나와야 한다.
def test(a, b, c):
    print("a :", a, end=", ")
    print("b :", b, end=", ")
    print("c :", c)
test(1, 2, 3) # 출력 => a : 1, b : 2, c : 3
test(b=2, c=4, a=5) # 출력 => a : 5, b : 2, c : 4
test(3, c=4, b=2) # 출력 => a : 3, b : 2, c : 4
# test(c=4, b=2, 3) 이러면 에러를 띄운다 (위치인자는 항상 키워드인자 앞에 나와야 한다.)


## 참고
# 함수 자체를 변수로 받을 수 있다.
def print_hello(name):
    print("Hello " + name)

print_hello_name = print_hello
print_hello_name('kyung')

func_list = [print_hello, 1, 2, 3]
func_list[0]('kyung')

func_dict = {
    'func' : print_hello,
    'test' : 11,
    'test2' : 'sss'
}
func_dict['func']('kyung')