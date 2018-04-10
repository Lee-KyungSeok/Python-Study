# map

## 모든 리스트에 1을 더하고 싶은 경우
a = list(range(1, 10+1))
## 이전 방법>
result = []
for el in a:
    result.append(el +1)

## map 이용
result = map(lambda x: x+1, a)
print(list(result))


### 예제> 
### 1~100이 담긴 리스트를 fizzbuzz 하기(3의 배수면 fizz, 5의 배수면 buzz, 15의 배수면 fizzbuzz)
listEx = (range(1, 20))
result = map(lambda x: 'fizzbuzz' if x%15==0 else ('fizz' if x%3==0 else ('buzz' if x%5==0 else x)), listEx)
print(list(result))