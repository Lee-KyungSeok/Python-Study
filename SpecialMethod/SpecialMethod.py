# 3. 몇가지 python 스페셜 메소드 (특정 이름으로 하면 어떤 기능을 수행)
## __str__()    : 자기 자신의 객체를 호출한다. (a 출력과 a.__str__() 는 동일)
## __call__()   : 인스턴스를 함수처럼 사용했을때 호출한다. ( a() 를 호출)
## __add()__(y) : 객체 + 객체 를 선언하면 이 메소드를 호출한다.

class SpecialMethod:
    money = 1000

    def __init__(self, name):
        print("스페셜 메소드 시작")
        self.owner = name
    
    def __str__(self):
        # print(객체명) 입력시 이를 호출
        return '__str__ 호출됨, {}의 지갑입니다.'.format(self.owner)
    
    def __repr__(self):
        # 레플 환경에서 객체만 입력시 호출
        return '__repr__ 호출됨, {}의 지갑입니다.'.format(self.owner)

    def __add__(self, another):
        return self.money + another.money

    def __call__(self):
        print("호출되었습니다.")

a = SpecialMethod('a')
b = SpecialMethod('b')
print(a + b) 
print(a())