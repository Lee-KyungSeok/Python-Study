# filter

## ex> 2의 배수만 거르는 경우
## 이전 방법
a = list(range(1, 10+1))
result = []
for el in a:
    if(el % 2 == 0):
        result.append(el)
    else:
        pass
print(result)

### filter 이용
filterResult = list(filter(lambda x : x%2==0, a))
print(filterResult)

### 예제
### 1~100 리스트에서 50보다 큰 값만 남긴 후 2의 배수만 가진 리스트 남기기
at = list(range(1,100+1))
result = filter(lambda x: x%2==0, (filter(lambda x: x>50, at)) )
print(list(result))