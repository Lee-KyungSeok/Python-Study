# Class
  - Class basic
  - Class 상속
  - Class 오버라이드
  - Python Special Method
    - \_\_init\_\_ / \_\_str\_\_ / \_\_repr\_\_ / \_\_add\_\_ / \_\_call\_\_

---

## Class basic
  ### 1. Class 기초
  - 파이썬은 객체지향으로 Class 형식으로 되어 있다.
  - 클래스란 공통된 인스턴스(객체)를 모아놓은 것(중복된 값을 모아놓아 공통의 인스턴스 이용 가능)
    - ex> Class : 지갑 (내 지갑, 친구 지갑 등 여러 지갑이 만들어 질 수 있다.)
  - Class 안에 있는 함수를 메서드라고 한다.
  - Class는 자동적으로 object를 상속받는다.
  - `self` : 클래스가 객체를 만들 때, 자기자신을 의미한다.

  ```Python
  class 클래스명:
      pass
  ```

  ### 2. 인스턴스 메서드, 클래스 메서드, \_\_init\_\_ 메서드
  - `__init__` : 처음 객체가 실행될 때 실행되는 메서드
  - 모든 인스턴스 메서드에는 항상 `self`(다른 변수로 선언 가능, but> self를 쓰는 것이 관용적)를 포함하며, 그 다음 필요한 인자를 넣어준다.
  - 클래스 메서드에는 `cls` 를 포함하며 classmethod 를 오버라이드 한다.

  ```Python
  # 인스턴스 메서드
  def print_message(self, message):
      print(message)

  # 클래스 메서드
  @classmethod
  def show_info(cls):
      print(cls.count);
  ```

  ### 3. 클래스 선언시 특징
  - 만든 클래스를 호출해서 인스턴스를 만든다.
  - => init 메소드를 실행한다.(생성자 느낌, self 는 파이썬에서 자동적으로 주므로 다음 파라미터부터 인자를 입력하여 클래스를 생성)
  - => name을 self.owner 에 넣으면 name 이라는 인자는 자신의 속성 중 owner에 이를 저장한다.
  - 다른 메소드도 self 라는 것을 받기 때문에 써주어야 한다. (꼭 self는 아니어도 되지만 첫번째 인자에는 항상 자기 자신이 들어간다. self로 쓰는 것이 관용적)

  ### 4. 클래스 예시
  - `__init__` 의 실행 메서드 이용
  - 인스턴스 메서드 이용
  - 클래스 메서드 이용

  ```Python
  class Wallet:
      money = 0
      count = 0

      def __init__(self, name):
          # owner = name 하게 되면 외부에서 사용 불가.
          self.owner = name
          print("{}님 환영합니다.".format(name))
          Wallet.count += 1

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

      @classmethod
      def show_wallet_count(cls):
          print("총 {} 개의 지갑이 생성됨".format(cls.count))

  my_wallet = Wallet('kyung')
  seok_wallet = Wallet('seok')

  my_wallet.print_owner_name() # 출력 : kyung
  seok_wallet.income(1000) # seok_wallet 에 1000을 추가
  Wallet.show_wallet_count() # 출력 : 총 2 개의 지갑이 생성됨
  ```  

---

## Class 상속과 오버라이드
  ### 1. Class 상속
  - 클래스를 상속하면 부모 클래스의 모든 기능을 가질 수 있다.
  - Class 는 기본적으로 object 를 상속하며 object 에 있는 메서드를 이용할 수 있다.
  - 클래스를 선언하고 괄호 안에 상속할 클래스를 넣어 생성한다.

  ```Python
  class Child(Parent):
      pass
  ```

  > 예시 (Wallet 을 상속받아 Account 생성)

  ```Python
  class Account(Wallet):
      def send_money(self, money, to):
          if self.money > money:
              to.money += money
              self.money -= money
              print("{}원을 {}에게 보냈습니다.".format(money,to.owner))
              self.print_now_money()
          else:
              print("잔액이 부족합니다.")
              self.print_now_money()

  my_account = Account('kyung')
  seok_account = Account('seok')

  my_account.income(10000)
  my_account.send_money(1000, seok_account) # 출력 : 100원을 seok 에게 보냈습니다
  ```

  ### 2. Class 오버라이드
  - 클래스를 상속받았을 때 부모에서 정의한 메서드를 다시 정의할 수 있다.
    - ex> `__init__`을 새로 정의하면 자식에서 정의한 init을 실행한다.
  - `super()` : 부모 클래스에 있는 메서드를 실행시킬 수 있다. (부모호출)

  ```Python
  class Account(Wallet):
      def __init__(self, name, account_number):
          self.account_number = account_number
          super().__init__(name)
          ''' 상속 메서드 추가 '''

  my_account = Account('kyung', '123-342343-12342') # 이렇게 사용
  ```

  ### 3. 다중 상속
  - 괄호 안에 두 가지 클래스를 넣어 상속할 수 있다.
  - 같은 메서드가 존재하면 먼저 상속한 클래스의 메서드를 호출한다.

  ```Python
  class A:
      def say_a(self):
          print("A!")
      def say_hi(self):
          print("hi! from A!")
  class B:
      def say_b(self):
          print("B!")
      def say_hi(self):
          print("hi! from B!")

  class C(A, b):
      pass

  c = C()
  c.say_hi() # 출력 : hi ! from A!
  ```

---

## 참고
  ### 1. issubclass
  - 클래스를 상속받았는지 확인 가능

  ```Python
  print(issubclass(ChildWallet,Wallet)) # True 반환
  print(issubclass(Wallet, object)) # True 반환
  print(issubclass(Wallet, int)) # False 반환
  ```

---

## Python Special Mehod
  ### 1. \_\_str\_\_
  - d

  ### 2. \_\_repr\_\_
  - d

  ### 3. \_\_add\_\_
  - d

  ### 4. \_\_call\_\_
  - d
