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
  data = [[1,2,3],[4,5,6],[7,8,9]]

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
  data = [[1,2,3],[4,5,6],[7,8,9]]

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
