# 파일 만들고 읽어오기 예제 (한번 함수로 만들어봄)
# Hello World 10번, Hello Python 10번 입력하고 각각 20번 10번 읽기

def writeFile(path, text):
    f = open(path, "w")
    f.write(text)
    f.close()

def appendFile(path, text):
    f = open(path, "a")
    f.write(text)
    f.close()

content = ""
for _ in range(10):
    content += "hello world!\n"
writeFile("./sample.txt", content)

for _ in range(10):
    appendFile("./sample.txt","hello python!\n")

for i in range(11):
    f = open("./sample.txt","r")
    if(i<10):
        content = f.readline()
        print(content, end="")
    else:
        f.seek(0)
        print(f.read())
        f.close()

# with를 쓴다면...
with open("./sample.txt","r") as f:
    for _ in range(10):
        print(f.readline(), end="")
with open("./sample.txt","r") as f:
    print(f.read())