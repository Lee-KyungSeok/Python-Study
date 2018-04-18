# numpy
  - numpy 사용하기 (ndarray)

---

## numpy (Numerical Python)
  ### 1. numpy 란?
  - 반복문 없이 빠른 벡터 계산을 제공하는 다차원 베열을 제공해주는 도구
  - C, C++, Fortran 으로 쓰여진 코드를 통합하는 도구
  - 설치 : `pip install numpy`
  - 사용 : `import numpy as np` (관용적으로 np로 사용한다.)

  ### 2. ndArray 생성
  - numpy 를 통해 생성되는 N차원 배열 객체
  - C로 되어 있어 빠르면서 유연한 자료구조
  - array() 안에 리스트, 튜플 등을 넣어준다.

  ```Python
  np.array([[1,2,3],[4,5,6]])  # 리스트
  np.array((1,2,3))           # 튜플
  np.array(range(10))         # range 사용
  np.arange(10)               # numpy 에서 제공하는 range
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy1.png)

  ### 3. 특정한 수로 초기화된 행렬 생성
  - `ones()` : 1 로 초기화
  - `zeros()` : 0 으로 초기화
  - `empty()` : 메모리를 초기화 시켜주지 않기때문에, 어떠한 값이 들어있을지 모름.

  ```Python
  np.ones(10)      # 1 로 이루어진 1차원 ndArray
  np.ones((3,3))   # 1 로 이루어진 3X3 ndArray
  np.zeros((3,3))  # 0 로 이루어진 3X3 ndArray
  np.empty((3,3))  # 3X3 ndArray
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy2.png)

  ### 4. Sclar 계산
  - 덧셈 : 각 요소에 값을 더해줌 (cf> 리스트는 에러 반환)
  - 곱셈 : 각 요소에 값을 곱해줌 (cf> 리스트는 배열의 개수를 곱셈만큼 추가시킴)
  - 데이터끼리 연산 : 각 요소에 맞는 데이터를 더함 (cf> 리스트는 데이터를 추가시킴)

  ```python
  data = np.array([[1,2,3],[4,5,6],[7,8,9]])

  data + 3
  data * 3
  data + data
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy3.png)

  ### 5. 차원, 행/열, 타입
  - `ndim` : 차원 리턴
  - `shape` : 행/열 리턴
  - ndArray 는 list 와 다르게 __동일한 타입__ 만 가실 수 있다는 것 주의!!
    - `dtype` : 타입 리턴
    - `astype(타입)` : 데이터 타입 변환

  ```python
  data = np.array([[1,2,3],[4,5,6],[7,8,9]])

  # 리턴값
  data.ndim   # 타입 리턴
  data.shape  # 행/열 리턴
  data.dtype  # 타입 리턴

  # ndArray 생성시 데이터 타입 지정
  data = np.array([1,2,3],dtype=np.float)

  # 데이터 타입 변환
  data.astype(np.unicode)
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy4.png)

  ### 6. indexing
  - `data[행][열]` : 행과 열로 요소를 뽑아 낼 수 있다.

  ```Python
  data = np.array([[1,2,3],[4,5,6],[7,8,9]])

  data[0]     # 하나만 뽑는 경우
  data[0][2]  # 일반적인 요소 뽑기
  data[0,2]   # 헹과 열을 이용하여 요소 뽑기
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy5.png)

  ### 7. slicing
  - `data[:N]` : 1차원 슬라이싱 (리스트에서는 이러면 error 호출)
  - `data[:N] = M` : N까지 슬라이싱된 부분들을 M으로 교체
  - `data[0:N]` : (2차원 이상에서) 행 기준으로 슬라이싱
  - `data[:, 0:N]` : (2차원 이상에서) 열 기준으로 슬라이싱
  - `data[data>N]` : boolean 슬라이스

  ```Python
  data1 = np.array([1,2,3,4,5])
  data2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

  # 1차원 슬라이싱
  data1[:3]           # 1차원 슬라이싱
  data1[:3] = 5       # 슬라이싱 된 부분값 바꾸기

  # 다차원 슬라이싱
  data2[0:2]          # 행 기준으로 슬라이싱
  data2[:, 0:2]       # 열 기준으로 슬라이싱
  data2[:, 0:2] = 3   # 슬라이싱 부분의 값만 바꾸기

  # boolean 슬라이싱
  data2[data2>4]      # 특정 조건에 맞는 값을 이용한 slice
  data2[data2<4] = 2  # 특정 조건에 맞는 값만 바꾸기
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy6.png)

  ### 8. 형태 바꾸기
  - `reshape` : ndArray 의 행/열의 갯수 변화
  - `T` : ndAray 를 transpose

  ```Python
  data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

  # 행/열 갯수 변화
  data.reshape(2,6)   # 2 X 6 로 변화
  data.reshape(1,12)  # 1 X 12 로 변화
  data.reshape(12)    # 12 X 1 로 변화

  # transpose
  data.T      # data를 transpose 함
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy7.png)

  ### 9. universal function
  - numpy 에서 제공하는 ndarray 고속함수 (민약 이 함수가 존재한다면 속도가 훨씬 빠르기 때문에 반드시 쓰도록 한다.)
  - `sqrt` : 제곱근
  - `square` : 제곱
  - `max` / `min` / `mean` : 최대 / 최소 / 평균

  ```Python
  data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

  np.sqrt(data)     # 제곱근
  np.square(data)   # 제곱
  np.max(data)      # 최대
  np.min(data)      # 최소
  np.mean(data)     # 평균

  # 응용해보기 (제곱이 100보다 큰거는 0으로 변경)
  data[np.square(data) > 100] = 0
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy8.png)

  ### 10. 행렬의 연산 / 단위행렬
  - `dot(data)` : 행렬의 곱셈 (A X A)
  - `eye(N)` : N 차 단위행렬

  ```python
  data = np.array([[1,2,3],[4,5,6],[7,8,9]])

  data.dot(data)  # 행렬 곱셈 (data X data)
  np.eye(3)       # 3차 단위행렬
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/numpy/picture/numpy9.png)
