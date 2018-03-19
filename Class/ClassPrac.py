# Class

# Wallet 이라는 클래스 생성
class Wallet:
    # 자기 자신의 돈
    # 지갑의 총 개수
    money = 0
    count = 0

    # 스페셜 메서드
    def __init__(self, name):
        # owner = name 하게 되면 외부에서 사용 불가.
        self.owner = name
        print("{}님 환영합니다.".format(name))
        Wallet.count += 1
    
    # 인스턴스 메서드
    def print_owner_name(self):
        print("owner name is :", self.owner)
    
    def print_now_money(self):
        print("현재 잔액은 :", self.money)
        
    def spend(self, m):
        if self.money > m:
            self.money -= m
            print("{}을 사용했습니다.".format(m))
            self.print_now_money()
        else:
            print("가지고 있는 돈이 부족합니다")
            self.print_now_money()
    
    def income(self, m):
        self.money += m
        print("{}를 벌었습니다.".format(m))
        self.print_now_money()
    
    # 클래스 메서드
    @classmethod
    def show_wallet_count(cls):
        print("총 {} 개의 지갑이 생성됨".format(cls.count))

my_wallet = Wallet('kyung')
seok_wallet = Wallet('seok')

my_wallet.print_owner_name()
seok_wallet.income(1000)
Wallet.show_wallet_count() 


'''
### 비교해볼 것
My_MONEY = [0]

def spend(m):
    if My_MONEY[0] > m:
        My_MONEY[0] -= m
        print("{}을 사용했습니다. 남은잔액 : {}".format(m, My_MONEY[0]))
    else:
        print("가지고 있는 돈이 부족합니다")

def income(m):
    My_MONEY[0] += m
    print("{}을 벌었습니다. 남은잔액 : {}".format(m, My_MONEY[0]))

# 내 지갑
my_wallet = {
    'money' : My_MONEY,
    'spend' : spend,
    'income' : income
}

'''

# 2. 클래스의 상속
## cf> 클래스는 자동적으로 object를 상속받는다.

## 사용법
## 클래스를 선언하고 괄호 안에 상속할 클래스를 넣는다.
## 상속을 하면 부모 클래스의 모든 기능을 모두 가질 수 있다.
### class Child(Parent):
###    pass

## ex>
class ChildWallet(Wallet):
    pass

k_w = ChildWallet('kyung')
k_w.print_owner_name() # owner name is : kyung 출력

## cf> issubclass : 클래스를 상속받았는지 확인
print(issubclass(ChildWallet,Wallet)) # True 반환
print(issubclass(Wallet, object)) # True 반환
print(issubclass(Wallet, int)) # False 반환

## ex2> Wallet을 상속받아 Account를 만들어 보자
class Account1(Wallet):
    def send_money(self, money, to):
        if self.money > money:
            to.money += money
            self.money -= money
            print("{}원을 {}에게 보냈습니다.".format(money,to.owner))
            self.print_now_money()
        else:
            print("잔액이 부족합니다.")
            self.print_now_money()

# 2-2 클래스 오버라이드

## ex>
class OverWalletEX1(Wallet):
    def __init__(self, name, account_number):
        self.owner = name
        self.account_number = account_number
        ''' 추가 '''

## super()를 이용해서 부모 클래스에 있는 메소드를 실행시킬 수 있다. (부모호출)
## ex>
class OverWalletEX2(Wallet):
    def __init__(self, name, account_number):
        self.account_number = account_number
        super().__init__(name)
        ''' 추가 '''