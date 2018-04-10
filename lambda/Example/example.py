from functools import reduce

# [1,2,3,4,5,6,7,8,9,10] 의 리스트를 예제와 같이 바꾸자
origin_list = list(range(1, 10+1))

# 1. [3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

result1 = map(lambda x: x+2, origin_list)
print(list(result1))

# 2. [1, 4, 9, 16, 25, 36, 49, 64 ,81, 100]
result2 = map(lambda x: x**2, origin_list)
print(list(result2))

# 3. [64, 81, 100]
result3 = filter(lambda x: x>7, origin_list)
result3 = map(lambda x: x**2, result3)
print(list(result3))

# 4. 55
result4 = reduce(lambda x, y: x+y, origin_list)
print(result4)
