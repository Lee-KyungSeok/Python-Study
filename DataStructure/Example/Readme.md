# DataStructure 문제 예시
  - 1. 알파벳별 출현 횟수 구하기
  - 2. List Comprehension

---

## 알파벳별 출현 횟수 구하기
  - 긴 글을 가져와서 알파벳별 출현 횟수 구하기

  ```Python
  long_values = """
  Contents
  Introduction
  A Foolish Consistency is the Hobgoblin of Little Minds
                  ...
  """

  results = {}
  # key를 초기화
  keys = []
  for i in "abcdefghijklmnopqrstuvwxyz":
      keys.append(i)
  # 값을 추출
  for i in long_values:
      if i in keys:
          if results.get(i):
              results[i] = results.get(i) + 1
          else:
              results[i] = 1
  print(results)
  ```

---

## List Comprehension
  - List Comprehension 예제

  ```Python
  results = []

  ## [1, 2, 3, 4, 5, 6]
  results = [i for i in range(1,7)]
  print(results)

  ## [6, 5, 4, 3, 2, 1]
  results = [i for i in range(1,7)]
  results.reverse()
  print(results)

  ## [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
  results = [ [j for j in range(1,4) ] for _ in range(3) ]
  print(results)

  ## [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  results = [[ j for j in range(i, i+3)] for i in range(1,10) if i%3 == 1]
  print(results)
  ```
