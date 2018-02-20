# <참고> Whitespace Character
# \n : 새로운 줄을 만들 때
# \t : 탭만큼 공간을 만들 때

# <참고> pprint : 리스트나, 딕셔너리를 알아보기 쉽게 출력해준다.
# import pprint
# pprint.pprint("값")

# File IO

# 1. open 이용

# 경로 : 상대경로 / 절대경로 존재
# 모드 : 파일을 새로 쓸건지, 읽을건지, 추가할건지 용도가 달라진다.
## - w : write 모드, 파일 전체에 새로 쓰기
## - r : read 모드, 파일을 읽는 모드
## - a : append 모드, 파일에 내용을 추가하는 모드

# f = open("파일경로", "모드") 
# f.close()

# 상대경로 - write
# 현재 디렉토리의 파일인 경우 "./" 을 경로로 지정 (파일이 없는 경우 생성된다.)
f = open("./hello.txt","w")
f.write("Hello World!")
f.close()  # hello.txt을 만들고 여기에 "Hello World!" 내용을 저장

# 상대경로 - append
f = open("./hello.txt", "a")
for i in range(2, 10+1):
    content ="\n" + str(i) + "번째 줄입니다."
    f.write(content)
f.close()  # hello.txt 파일에 작성한 내용들을 추가

# 상대경로 - read
f = open("./hello.txt", "r")
content = f.read()
print(content)
# print(f.read()) # 파일을 읽을때 파일을 읽을 때 다 읽은 후 커서의 위치가 마지막을 가르키기 때문에 읽히지 않는다.
f.seek(0) # 이는 0번째 글자로 커서를 옮겨 주는 메소드로 다시 read 할 수 있게 된다.
f.close()  # hello.txt 파일에 저장된 내용을 읽는다.

# 절대경로 ("윈도우의 경우 \\ 두개 씩 작성해야 한다. => \ 만 사용할 경우 다른 escape가 들어갈 수도 있다고 착각할 수도 있기 때문")
f2 = open("C:\\workspaces\\Python\\FileIO\\hello.txt", "r")
content2 = f2.read()
print(content2)
f2.close()

# readline 메소드 : 한줄씩 읽는다.
f = open("./hello.txt", "r")
print(f.readline())
print(f.readline())
f.close()


# 2. with
#  : 자동으로 닫아주는 기능을 한다. (close를 자동으로 실행해준다)
#  : 이는 enter와 exit 이라는 메소드를 실행하는 기능을 한다. (class에서 다시 생각해볼 것)
# with open("path", "mode") as f:
#   로직 작성 (ex> f.write)
with open("./new.txt", "w") as f:
    f.write("안녕하세요! with입니다.")
if not f.closed:
    print("파일을 꺼야합니다")
else:
    print("파일이 꺼져있습니다.")