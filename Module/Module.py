# Module
# 프로그램(기능)의 모음 => 기능들을 모듈화 시킬 수 있다.
# 이 모듈을 불러올 수 있는 이유는 "sys.path" 에 경로가 등록되어 있기 때문이다.
# sys.path의 첫번째는 '' 가 저장되며 현재 경로를 등록한다. 만약 이것이 지워졌다면 사용자가 정의한 모듈을 import 할 수 없게 된다.

# from ** import ***
# 혹은 import ***

# 사용 예시
from Mmulti import multi_all
import Msum

print(multi_all(1,2,3,4,5)) # 120 출력
print(Msum.add_1(100)) # 101 출력

# __name__
print(__name__) # 출력 : main
Msum.namePrint() # 출력 : Msum (but> Msum.py를 직접 하면 main 출력)

## 아래와 같이 메인일 경우에(모듈이 아닐 경우에)만 실행시킬 수 있는 로직 작성이 가능하다.
if __name__ == "__main__":
    print("이 파일이 실행(내가 메인임)")


# <참고> dir 함수
## 그 객체에 어떠한 기능 혹은 값들이 있는지 알 수 있다.
print(dir(1)) # 출력 : int가 가진 메소드들을 보여준다.
print(dir("")) # 출력 : String 이 가진 메소드들을 보여준다.