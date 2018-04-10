# reduce
## ex>
from functools import reduce

a=list(range(10+1))
result = reduce(lambda x, y: x+y, a)
print(result) ## 출력 : 55 
##=> [0,1,2,3,4,5,6,7,8,9,10] => [1,2,3,4,5,6,7,8,9,10] => [3,3,4,5,6,7,8,9,10] => [6,4,5,6,7,8,9,10] => ... => [45,10] => 55

### 예제
### 1~10까지 가진 리스트에서 각 요소의 제곱을 더하기
a=list(range(1, 10+1))
result = reduce(lambda x, y: x**2 + y**2, a)