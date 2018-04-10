import random
from functools import wraps

class Wallet:
    money = 0;
    count = 0;

    def __init__(self, name):
        self.owner = name
        print('{}님 환영합니다'.format(name))
        Wallet.count +=1
    def print_owner_name(self):
        print('이름 :',self.owner)
    def print_now_money(self):
        print('잔액 :', self.money)
    def spend(self, m):
        if self.money >m:
            self.money -= m
            self.print_now_money()
        else:
            print("가지고 있는 돈이 부족합니다.")
            self.print_now_money()
    def income(self, m):
        self.money +=m
        self.print_now_money()
    @classmethod
    def show_wallet_count(cls):
        print(cls.count)

# 1. account class 에 다음 기능을 추가
'''
1. 계좌 생성시에 password 지정 및 은행이름 입력.
2. 송금시에 password 입력 및 일치하는지 확인
3. 송금시에 같은 은행이 아닌 경우에는 수수로 -500 원 별도 부여
4. 소유자가 같은 계좌는 + 연산자로 보유금액 합산가능
5. 소유자가 같은지 == 연산자 혹은 != 연산자로 확인가능
'''
'''
class Account(Wallet):
    def __init__(self, name, account_address, password, bank):
        self.account_address = account_address
        self.password = password
        self.bank = bank
        super().__init__(name)

    def check_password(self, password):
        return password == self.password

    def bank_fee(self, bank):
        if bank != self.bank:
            return 500
        else:
            return 0

    def send_money(self, money, to, password):
        if self.check_password(password) != True:
            print('비밀번호가 일치하지 않습니다.')
            return

        if self.money> money + self.bank_fee(to.bank):
            to.money += money
            self.money = self.money - money - self.bank_fee(to.bank)
            print('내 돈 :', self.money, '/', '보낸사람 총액 :', to.money)
        else:
            print('잔액 부족')
            self.print_now_money()
    def check_owner(self, owner):
        return self.owner == owner

    def check_my_total_money(self, account):
        if self.check_owner(account.owner):
            print(sum([account.money, self.money]))
        else:
            print("소유주가 일치하지 않습니다.")
'''

# 2. bank Class 만들기
'''
1. 은행 대표번호와, 계좌 번호 생성 패턴을 입력하여 인스턴스 생성
    예) shinhan = Bank(’02-1234-1234’, ‘xxx-xxxx-xxxx’)
2. 계좌 번호 생성하는 메소드를 만들어서 입력받은 패턴대로 랜덤한 숫자를 더하여 계좌번호 리턴
3. 업그레이드된 Account Class에서 인스턴스 생성시 bank인스턴스도 같이 입력, bank instance의 메소드를 사용하여계좌 번호 자동생성되게 조정
4. 에러 발생시 은행 대표번호가 출력되어 문의 가능하도록 예외처리
'''

class bank():
    def createAccount(self, bankName):
        account = ''
        if bankName == 'shinhan':
            account += '02-'
        elif bankName == 'hana':
            account += '11-'
        elif bankName == 'woori':
            account += '12-'
        else:
            account += '00-'
        account = account + str(random.randint(1000,9999)) + '-' + str(random.randint(1000,9999))
        return account
    
    def call_number(self, bankName):
        if bankName == 'shinhan':
            return '02-1234-5678'    
        elif bankName == 'hana':
            return '02-9874-1546'
        elif bankName == 'woori':
            return '02-4567-5699'
        else:
            return '00-0000-0000'
            

class Account(Wallet):
    def __init__(self, name, password, bankName, bankInstance):
        self.account_address = bankInstance.createAccount(bankName)
        self.bankName = bankName
        self.phone = bankInstance.call_number(bankName)
        self.password = password
        self.bank = bank
        super().__init__(name)
    
    def exceptProcess(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                print('오류! 전화 :', phone)
                return
    
    @exceptProcess
    def check_password(self, password):
        return password == self.password

    @exceptProcess
    def bank_fee(self, bankName):
        if bankName != self.bankName:
            return 500
        else:
            return 0

    @exceptProcess
    def send_money(self, money, to, password):
        if self.check_password(password) != True:
            print('비밀번호가 일치하지 않습니다.')
            return

        if self.money> money + self.bank_fee(to.bankName):
            to.money += money
            self.money = self.money - money - self.bank_fee(to.bankName)
            print('내 돈 :', self.money, '/', '보낸사람 총액 :', to.money)
        else:
            print('잔액 부족')
            self.print_now_money()

    @exceptProcess
    def check_owner(self, owner):
        try:
            return self.owner == owner
        except:
            print('!!!')

    @exceptProcess
    def check_my_total_money(self, account):
        if self.check_owner(account.owner):
            print(sum([account.money, self.money]))
        else:
            print("소유주가 일치하지 않습니다.")

# bank instance 생성
bankInstance = bank()
a = Account('kyung', '1234', 'shinhan', bankInstance)
b = Account('lee', '1234', 'woori', bankInstance)
c = Account('me', '1234', 'shinhan', bankInstance)