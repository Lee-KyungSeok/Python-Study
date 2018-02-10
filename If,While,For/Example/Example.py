# 글씨 반대로 출력
n = list(input("글씨입력"))
n.reverse()
for i in n:
    print(i, end="")

# Palindrome
while True:
    n = input("판별하고자 하는 문자를 입력해주세요 / 종료하고 싶다면 exit 입력")
    if n == "exit":
        break
    else:
        key = True
        word = list(n.lower().replace(" ",""))
        compare = (word.copy())
        compare.reverse()
        print(word)
        print(compare)
        for i in range(len(word)):
            if word[i] != compare[i]:
                key = False
                break
        if key:
            print("Palindrome 입니다.")
        else:
            print("Palindrome이 아닙니다.")