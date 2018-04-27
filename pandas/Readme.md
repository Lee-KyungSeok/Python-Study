# pandas
  - pandas 사용하기

---

## pandas
  ### 1. pandas 란?
  - 고수준의 자료구조
  - Numpy 기반으로 개발되어 빠른 연산 가능
  - 설치 : `pip install pandas`
  - `Series` 와 `DataFrame` 이 존재
  - 호출

  ```Python
  from pandas import Series, DataFrame
  import pandas as pd
  import numpy as np # numpy 기반이기 때문에 이도 호출
  ```

---
## Series
  ### 1. 선언
  - numpy 자료형을 담는 1차원 자료구조

  ```Python
  data = Series([5,4,3,-1,9])
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/pandas/picture/pandas.png)

  ### 2. values / type / index
  - `values` : ndarray 로 반환
  - `type` : type을 알려줌
  - `index` : index를 반환

  ```Python
  data.values           # 출력 : array([ 5,  4,  3, -1,  9], dtype=int64)
  type(data.values)     # 출력 : numpy.ndarray
  data.index            # 출력 : RangeIndex(start=0, stop=5, step=1)
  ```

  ### 3. index 지정
  - index 를 커스텀해서 지정해줄 수 있다.

  ```Python
  data = [5,4,3,-1,9]
  data2 = Series(data, index=['a','b','c','d','e'])

  data2.index
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/pandas/picture/pandas2.png)

  ### 4. 값 불러오기
  - 한가지 값 : `data[a]` , `data.a`
    - 리턴은 특정 값으로
  - 여러 컬럼값 얻기 ([[]] 를 이용) : `data[['a','b']]`
    - 리턴은 같은 데이터 형식

  ```Python
  # 한 가지 값
  data2['a']
  data2.c

  # 여러 값
  data2[['a','b']]
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/pandas/picture/pandas3.png)

  ### 5. numpy 내장함수 이용하기
  - sqrt / sum 등 이용 가능

  ```python
  np.sqrt(data2[['a','b']])
  np.sum(data2)
  ```

  ### 6. for 문에서 사용
  - dictionary 와 다르게 Series 는 value를 가져온다. (dictionary는 key를 가져옴)

  ```python
  for what in data2:
      print(what)  # 5,4,3,-1,9 가 차례로 나옴 (dictionary 라면 a,b,c,d,e 가 나옴)
  ```

  ### 7. dictionary를 Series 로 변환
  - dictionary를 인자로 넣는다.
  - 원하는 순서가 있다면, index에서 지정할 수 있다. (값이 없다면 NaN)

  ```python
  product_and_price = {'choco_ball' : 2500, 'gum':700, 'bbabbaro' : 1700, 'sacomdalcom' : 500}
  product_series = Series(product_and_price, index=['choco_ball', 'gum', 'bbabbaro', 'sacomdalcom', 'potatto_chip'])
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/pandas/picture/pandas4.png)

  ### 8. Null 확인
  - `isnull()` : null이라면 True 반환
  - `notnull()` : null 이라면 False 반환

  ```python
  # null 확인
  product_series.isnull()
  # not null 확인
  product_series.notnull()

  # null 인것들을 0으로 세팅
  product_series[product_series.isnull()] = 0
  ```

  ### 9. Series 의 name 지정
  - `.name` : 데이터의 name 지정
  - `.index.name` : 인덱스의 name 지정

  ```python
  # name 변경
  product_series.name = 'price'
  # index의 name 변경
  product_series.index.name = 'product name'
  ```

  ### 10. 인덱스의 순서 변경 / 값 지우기
  - `reindex` : 인덱스의 순서 변경
  - `drop` : 값 지우기
  - 원본 변경이 아니라 바뀐것을 리턴

  ```Python
  # 인덱스의 순서 변경
  product_series2 = product_series.reindex(['gum', 'choco_ball', 'sacomdalcom', 'potatto_chip', 'bbabbaro'])

  # 값 지우기
  product_series3 = product_series2.drop('gum')
  ```

  ### 11. slicing
  - 일반 인덱싱과는 다르게 마지막을 포함해서 slicing 함

  ```python
  # slicing
  product_series3['sacomdalcom':'bbabbaro'] # sacomdalcom 과 bbabbaro 를 포함해서 그 사이값들 slicing

  # slicing 후 할당
  product_series3['sacomdalcom':'potatto_chip'] = 2000
  ```

---
## DataFrame
  ### 1. 선언
  - 표/엑셀 형태의 자료구조 (1차원 Series들의 모임, 2차원)

  ```python
  data = {
      'name' : ['gum', 'choco_ball', 'potatto_chip', 'bbabbaro'],
      'price' : [1600,700,2500,200],
      'made' : ['a','a','b','c']
  }
  df = DataFrame(data, columns = ['name', 'price', 'made'], index=[1,2,3,4])
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/pandas/picture/pandas5.png)

  ### 2. 특정 데이터 불러오기
  - column 불러오기
    - `[index]` , `.index` : 리턴을 Series 로 함
    - `[[index]]` : 리턴이 데이터 프레임
    - `[[index ,index ]]` : 두개 이상 불러오기
  - row 불러오기
    - `.ix[index]` : index 를 가지는 row를 불러옴
    - `.ix[[index,index]]` : 두개 이상 불러오기

  ```python
  # Series
  df['name']
  df.price
  # DataFrame
  df[['name']]
  df.ix[1]

  # 두개 이상인 경우
  df[['name','price']]
  df.ix[[2,3], ['name', 'price']]
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/pandas/picture/pandas6.png)

  ### 3. slicing
  - slicing 가능

  ```Python
  df[:3]
  df[df['price']>1000]
  df[df['price']>1000].name # name 칼럼만 출력
  ```

  ### 4. column 및 row 추가, transpose
  - 추가 : column 은 [] , row는 ix 를 사용
  - transpose : `T` 이용

  ```python
  # 칼럼 추가
  df['amount'] = 100

  # row 추가
  df.ix[5] = ['sacomdalcom', 600, 'b', 100]  

  # transpose
  df2 = df.T
  ```

  ### 5. index 순서 바꾸기, 지우기
  - column index, row index 를 바꿀 수 있다.
  - `drop` : 지우기 (column 인경우 axis를 1로 지정하여 칼럼이라고 알려줘야 함)

  ```python
  # row 순서 바꾸기
  df3 = df.reindex([5,3,1,4,3])
  # column 순서 바꾸기
  df3 = df3.reindex(columns=['price', 'name', 'amount', 'made'])

  # 2번 index 삭제 (row)
  df = df.drop(2)
  # made 인 column 삭제
  df = df.drop('made', axis=1)
  ```

  ### 6. numpy 연산 가능
  - ex> sum

  ```python
  np.sum(df.amount)
  ```

  ### 7. 표를 html 로 변경
  - `to_html` : 표를 html로 변경

  ```python
  df.to_html()
  ```
