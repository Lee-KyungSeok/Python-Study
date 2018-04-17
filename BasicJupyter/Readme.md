# Basic Jupyter
  - Jupyter notebook 사용
  - requests
  - beautifulsoup4
  - robots.txt

---

## Jupyter notebook
  ### 1. jupyter notebook
  - REPL 환경으로 바로 결과를 확인 가능
  - 이전 코드 및 여러줄의 코드 쉽게 작성 가능
  - 이미지 및 그래프를 한 화면 내에 띄울 수 있고 Markdown 등 다양한 기능 제공
  - 보통 데이터 분석이나 머신러닝에 많이 활용됨

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/BasicJupyter/picture/jupyter.png)

  ### 2. 설치 및 실행
  - 설치

  ```
  pip install jupyter
  pip3 install jupyter  (Mac 인 경우)
  ```

  - 실행

  ```
  jupyter noteobook
  ```

  ### 3. 몇가지 tip
  - 제어모드과 입력모드가 존재
    - 제어모드을 `1n` 부분 클릭시 __파란색__ 으로 바뀜
    - 입력모드 일반 입력하는 부분으로 __초록색__ 으로 바뀜
  - 무한루프를 돌리게 되면 `In` 부분이 * 로 바뀌게 된다.
  - 코드를 실행하는 단축키는 `Shift + Enter`
  - 삭제하고 싶을 때는 제어모드로 설정 후 `dd`
  - 코드를 중간에 추가시키고 싶을 때는 삽입할 줄 위의 입력창을 클릭하고 메뉴의 `+` 버튼을 클릭
  - 제어모드에서 `m` 입력시 마크다운 언어로 변경, 다시 돌리려면 `y` 입력

  ### 4. 주의사항
  - 내장함수를 변수로 선언하지 않도록 조심!! => 변수로 선언하면 내장함수를 쓸 수 없게 된다.
  - 만약 실행 했다면 `builtins` 모듈을 불러와서 다시 설정하거나, jupyter notebook 을 껐다 켜야 한다.
  - jupyter notebook 은 평상시에 메모리를 많이 잡아먹으므로 쓰지 않으면 꺼두도록 하자

  > str 함수를 선언해 버린 경우 다시 설정

  ```python
  import builtins
  str = builtins.str
  ```

---
## requests
  ### 1. requests 란
  - 특정 url에 정보를 요청하여 결과를 받는 모듈

  ### 2. requests 설치
  - Mac 은 pip3 로 입력

  ```
  pip install requests
  ```

  ### 3. 사용 방법
  - 모듈을 불러와서 `get` 을 이용해 가져올 수 있으며, `text` 입력 시 내용을 가져온다.

  ```python
  import requests
  response = requests.get("주소")
  response # Status 코드를 불러옴
  response.text # 내용을 불러옴
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/BasicJupyter/picture/requests.png)

---

## beautifulsoup4
  ### 1. beautifulsoup4 란
  - 받아온 html string 정보를 분석해주는 도구

  ### 2. 설치

  ```
  pip install beautifulsoup4
  ```

  ### 3. 사용 방법
  - 모듈을 불러와서 text 값을 넣고 인코딩한다. (html로 인코딩)
  - 특정 태그의 값을 불러 올 수 있다. (그냥 하면 맨 첫번째를 불러온다.)
  - text 를 같이 하면 태그를 지우고 보여준다.
  - 사용시에는 `BeautifulSoup` 모듈을 불러와야 함에 주의

  ```python
  from bs4 import BeautifulSoup as bs # as 란 모듈을 bs.xxx 로 쓰기 위해 다시 명명하는 것
  result = bs(response.text, "html.parser") # html 을 가져옴
  result  # 전체 내용을 깔끔하게 가져옴
  result.title  # 내용 중 title 태그를 가져옴
  result.title.text # title 태그에서 내용만을 가져옴
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/BasicJupyter/picture/beautifulsoup.png)

---
## robots.txt
  ### 1. robots.txt 란?
  - 인터넷 검색엔진 배제 표준(Robots Exclusion Protocol)이란 보안이 필요한 내용이 검색엔진에 유출되지 못하도록 웹 페이지를 작성하는 방법을 기술한 국제기술 표준
  - 모든 검색로봇이 이 표준을 따르지는 않지만 일반 웹 사이트 개발자들이 손쉽게 적용할 수 있어 이용이 확산
  - 서버관리자가 웹페이지 HTML 작성시 맨 위에 검색로봇을 배제한다는 의미의 'File:robots.txt', 'User-agent: * /' 등을 적어놓으면 검색로봇의 검색 대상에서 제외

  ### 2. robots.txt 위치
  - robots.txt를 적용할 웹사이트의 최상위 디렉토리에 적용

  ```
  ex) www.kyung.com/robots.txt
  ```

  ### 3. 형식
  - `User-agent` : 검색봇 이름
  - `Disallow` : 접근 설정
  - `Crawl-delay` : 다음방문까지의 디레이(초)
  - `*`(와일드카드)는 모든 로봇을 뜻하며, `/`(슬래시)는 모든 디렉토리를 뜻함

  > 예시 1 - 구글, 다음 이외 모든 봇 차단

  ```
  User-agent: Googlebot
  Disallow:

  User-agent: Daumoa
  Disallow:

  User-agent: *
  Disallow: /
  ```

  > 예시 2 - 모든 봇 허용

  ```
  User-agent: *
  Disallow:
  ```

  > 예시 3 - 홈페이지 디렉토리의 일부만 검색엔진에 노출

  ```
  User-agent: *
  Disallow: /conection/
  Disallow: /my_conection/
  ```
