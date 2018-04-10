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

## Container
  ### 1. `__len__(self)`
  - 컨테이너의 길이를 반환
  - 불변 및 가변 컨테이너에 대한 프로토콜의 일부

  ### 2. `__getitem__(self, key)`
  - `self[key]` 표기법을 사용하여 항목에 액세스할 때의 동작을 정의
  - 가변 컨테이너 프로토콜과 불변 컨테이너 프로토콜의 일부
  - 적절한 예외를 발생시켜야 함( 키의 유형이 잘못된 경우 `TypeError`, 키에 해당하는 값이 없는 경우 `KeyError를` 지정)

  ### 3. `__setitem__(self, key, value)`
  - `self[nkey] = value` 표기법을 사용하여 항목이 할당된 경우의 동작을 정의
  - 이것은 가변 컨테이너 프로토콜의 일부
  - `KeyError` 와 `TypeError` 를 적절히 발생시켜야 함

  ### 4. `__delitem__(self, key)`
  - 항목이 삭제 된 경우의 동작을 정의합니다(ex> `del self[key]` )
  - 가변 컨테이너 프로토콜의 일부
  - 유효하지 않은 키가 사용되면 적절한 예외를 발생시켜야 함

  ### 5. `__iter__(self)`
  - 컨테이너에 대한 반복자를 반환해야 함
  - iter() 내장 함수와 for x in container: 형태를 사용하여 컨테이너가 반복될 때 가장 많이 볼 수 있다.
  - 반복자는 자체가 객체이며 자체를 반환하는 `__iter__` 메서드를 정의해야 함

  ### 6. `__contains__(self, item)`
  - `in` 과 `not in` 을 사용하여 멤버십 테스트에 대한 동작을 정의
  - 시퀀스 프로토콜의 일부가 아님

---

## Operator의 Special Method
  ### 1. Binary Operators

  Operator | Method | 비고
  :----: | :----: | :----:
  \+ | object.\_\_add\_\_(self, other) |
  \- | object.\_\_sub\_\_(self, other) |
  \* | object.\_\_mul\_\_(self, other) |
  // | object.\_\_floordiv\_\_(self, other) |
  / | object.\_\_div\_\_(self, other) |
  % | object.\_\_mod\_\_(self, other) |
  ** | object.\_\_pow\_\_(self, other) |
  \>\> | object.\_\_lshift\_\_(self, other) |
  << | object.\_\_rshift\_\_(self, other) |
  & | object.\_\_and\_\_(self, other) |
  ^ | object.\_\_xor\_\_(self, other) |
  \| | object.\_\_or\_\_(self, other) |

  ### 3. Extended Assignments

  Operator | Method | 비고
  :----: | :----: | :----:
  \+= | object.\_\_iadd\_\_(self, other) |
  \-= | object.\_\_isub\_\_(self, other) |
  \*= | object.\_\_imul\_\_(self, other) |
  //= | object.\_\_ifloordiv\_\_(self, other) |
  /= | object.\_\_idiv\_\_(self, other) |
  %= | object.\_\_imod\_\_(self, other) |
  \*\*= | object.\_\_ipow\_\_(self, other) |
  \>\>== | object.\_\_ilshift\_\_(self, other) |
  <<== | object.\_\_irshift\_\_(self, other) |
  &= | object.\_\_iand\_\_(self, other) |
  ^= | object.\_\_ixor\_\_(self, other) |
  \|= | object.\_\_ior\_\_(self, other) |

  ### 4. Unary Operators

  Operator | Method | 비고
  :----: | :----: | :----:
  \- | object.\_\_neg\_\_(self, other) | 단항 연산자
  \+ | object.\_\_pos\_\_(self, other) | 단항 연산자
  abs() | object.\_\_abs\_\_(self, other) |
  ~ | object.\_\_invert\_\_(self, other) | 비트 반전
  complex() | object.\_\_complex\_\_(self, other) | 리턴 값은 반드시 복소수값
  int() | object.\_\_int\_\_(self, other) | 리턴은 반드시 정수
  long() | object.\_\_long\_\_(self, other) | 리턴은 반드시 Long
  float() | object.\_\_float\_\_(self, other) | 리턴은 반드시 실수
  oct() | object.\_\_oct\_\_(self, other) | 리턴은 반드시 문자열
  hex() | object.\_\_hex\_\_(self, other) | 리턴은 반드시 문자열

  ### 5. Comparion Operators

  Operator | Method | 비고
  :----: | :----: | :----:
  < | object.\_\_lt\_\_(self, other) |
  <= | object.\_\_le\_\_(self, other) |
  == | object.\_\_eq\_\_(self, other) |
  != | object.\_\_ne\_\_(self, other) |
  \>= | object.\_\_ge\_\_(self, other) |
  \> | object.\_\_gt\_\_(self, other) |
