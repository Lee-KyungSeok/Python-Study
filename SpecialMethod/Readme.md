# Python Specail Method
  - \_\_init\_\_ / \_\_str\_\_ / \_\_repr\_\_
  - \_\_add\_\_ / \_\_call\_\_

---

## Python Specail Method
  ### 1. `__init__`
  - 처음 객체가 실행될 때 실행되는 메서드

  ```Python
  class SpecialMethod:
      def __init__(self, name):
          print("스페셜 메소드 시작")
          self.owner = name
  ```

  ### 2. `__str__`
  - 자기 자신의 객체를 호출 (a 출력과 a.\_\_str\_\_() 는 동일)
  - print(객체명) 입력시 호출

  ```Python
  class SpecialMethod:
      money = 1000
      def __init__(self, name):
          self.owner = name

      def __str__(self):
          return '__str__ 호출됨, {}의 지갑입니다.'.format(self.owner)
  ```

  ### 3. `__repr__`
  - 레플 환경에서 객체만 입력시 호출

  ```Python
  class SpecialMethod:
      money = 1000
      def __init__(self, name):
          self.owner = name

      def __repr__(self):
        return '__repr__ 호출됨, {}의 지갑입니다.'.format(self.owner)
  ```

  ### 4. `__add__`
  - 객체 + 객체 선언 시 호출

  ```Python
  class SpecialMethod:
      money = 1000

      def __init__(self, name):
          self.owner = name

      def __add__(self, another):
          return self.money + another.money
  a = SpecialMethod('a')
  b = SpecialMethod('b')
  print(a + b) # 출력 : 2000
  ```

  ### 5. `__call__`
  - 인스턴스를 함수처럼 사용했을 때 호출 (a() 호출)

  ```Python
  class SpecialMethod:
      money = 1000

      def __init__(self, name):
          print("스페셜 메소드 시작")
          self.owner = name

      def __call__(self):
          print("호출되었습니다.")
  a = SpecialMethod('a')
  print(a()) # 호출되었습니다 \n None 출력
  ```

---

## 그외 특징적인 Special Method
  ### 1. Binary Operators

  Operator | Method
  :----: | :----:
  \+ | object.\_\_add\_\_(self, other)
  \- | object.\_\_sub\_\_(self, other)
  \* | object.\_\_mul\_\_(self, other)
  // | object.\_\_floordiv\_\_(self, other)
  / | object.\_\_div\_\_(self, other)
  % | object.\_\_mod\_\_(self, other)
  ** | object.\_\_pow\_\_(self, other)
  \>\> | object.\_\_lshift\_\_(self, other)
  << | object.\_\_rshift\_\_(self, other)
  & | object.\_\_and\_\_(self, other)
  ^ | object.\_\_xor\_\_(self, other)
  \| | object.\_\_or\_\_(self, other)

  ### 2. Extended Assignments

  Operator | Method
  :----: | :----:
  \+= | object.\_\_iadd\_\_(self, other)
  \-= | object.\_\_isub\_\_(self, other)
  \*= | object.\_\_imul\_\_(self, other)
  //= | object.\_\_ifloordiv\_\_(self, other)
  /= | object.\_\_idiv\_\_(self, other)
  %= | object.\_\_imod\_\_(self, other)
  \*\*= | object.\_\_ipow\_\_(self, other)
  \>\>== | object.\_\_ilshift\_\_(self, other)
  <<== | object.\_\_irshift\_\_(self, other)
  &= | object.\_\_iand\_\_(self, other)
  ^= | object.\_\_ixor\_\_(self, other)
  \|= | object.\_\_ior\_\_(self, other)

  ### 3. Unary Operators

  Operator | Method
  :----: | :----:
  \- | object.\_\_neg\_\_(self, other)
  \+ | object.\_\_pos\_\_(self, other)
  abs() | object.\_\_abs\_\_(self, other)
  ~ | object.\_\_invert\_\_(self, other)
  complex() | object.\_\_complex\_\_(self, other)
  int() | object.\_\_int\_\_(self, other)
  long() | object.\_\_long\_\_(self, other)
  float() | object.\_\_float\_\_(self, other)
  oct() | object.\_\_oct\_\_(self, other)
  hex() | object.\_\_hex\_\_(self, other)

  ### 4. Comparion Operators

  Operator | Method
  :----: | :----:
  < | object.\_\_lt\_\_(self, other)
  <= | object.\_\_le\_\_(self, other)
  == | object.\_\_eq\_\_(self, other)
  != | object.\_\_ne\_\_(self, other)
  \>= | object.\_\_ge\_\_(self, other)
  \> | object.\_\_gt\_\_(self, other)
