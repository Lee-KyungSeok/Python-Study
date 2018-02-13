# 1. all, any 함수 직접 구현
def mAll(*args):
    result = True
    for i in args:
        if i == False:
            result = False
            break
        else:
            pass
    return result
print(mAll(True, True, True)) # 출력 : True
print(mAll(True, True, False)) # 출력 : False

def mAny(*args):
    result = False
    for i in args:
        if i == True:
            result = True
            break
        else:
            pass
    return result
print(mAny(False, False, False)) # 출력 : False
print(mAny(True, False, False)) # 출력 : True

# 2. 제곱근의 근사값을 구하는 재귀함수
def mRoot1(b, a = 7):
    if abs(a**2 - b) < 0.0001: # 한없이 가깝다면 조건
        return a
    else:
        a = (a+(b/a))/2
        return mRoot1(b, a)
print(mRoot1(27)) # 출력 : 5.19615480243797

# 3. 제곱근의 근사값을 구하는 재귀함수를 만들되, “한 없이 가깝다면” 을 “전에 값과 변함이 없다면" 으로 조건을 바꿔 만들어보세요
def mRoot2(b, a = 7):
    if a**2 == b:
        return a
    else:
        temp = (a+(b/a))/2
        if temp**2 == a**2: # 전에 값과 변함이 없다면 조건
            return a
        else:
            return mRoot2(b, temp)
        
print(mRoot2(27)) # 출력 : 5.196152422706632

# 4. isnumeric() 메소드 직접 구현
def mIsnumeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
print(mIsnumeric("1.124")) # 출력 : True
print(mIsnumeric("십사")) # 출력 : False