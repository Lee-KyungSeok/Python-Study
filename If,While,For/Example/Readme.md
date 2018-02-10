# 조건문(if), 반복문(while, for) 문제 예시
  - 글자 반대로 쓰기
  - Palindrome

---

## 글자 반대로 쓰기
  -  입력한 글자를 반대로 출력되도록 작성

  ```Python
  n = list(input("글씨입력"))
  n.reverse()
  for i in n:
      print(i, end="")
  ```

---

## Palindrome
  - 입력된 글자를 반대로 했을 때 동일하면 True, 아니면 False

  ```Python
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
  ```
