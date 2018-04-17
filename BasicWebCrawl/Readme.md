# Basic Web Crawl
  - 기본적인 Web Crawling

---

## Web Crawl 기본
  ### 1. 타입 인코딩
  - 특정 웹페이지에서는 한글등 다른 언어를 지원하지 않는 경우가 있다. 이 경우 `utf-8` 형식으로 인코딩 해주어야 한다.
  - 인코딩 하는 경우 먼저 바이트 타입으로 가져온 후 변환한다.
  - 참고
    - `type(response.text)` : str 타입 출력
    - `type(response.content)` : bytes 타입 출력

  ```python
  # 모듈
  import requests
  response = requests.get("url 주소")
  content = str(response.content, 'utf-8')
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/BasicWebCrawl/picture/crawl1.png)

  ### 2. 특정 태그만 가져오기
  - __beautifulsoup__ 모듈을 활용하여 가져올 수 있다.
  - `find` : 해당 조건에 만족하는 첫번째 요소를 리턴
  - `find_all` : 해당 조건을 만족하는 모든 요소를 리스트에 넣어서 리턴
  - 두번째 인자에 dicionary를 넣어 가져올 수 있다.
  - find_all 의 경우 일치하는 값이 1개든 0개든 __리스트__ 를 리턴함에 주의

  ```python
  from bs4 import BeautifulSoup as bs
  result = bs(content, 'html.parser')

  result.find('li')     # 첫번째 li 태그를 가진 요소를 리턴
  result.find_all('li') # 모든 li 태그를 가진 요소를 리턴

  result.find("li", {'id': 'best'}) # li 태그를 가지고 id가 best 인 요소를 리턴
  result.find_all("li", {'id': 'best'}) # li 태그를 가지고 id가 best 인 요소를 "리스트" 로 리턴

  # li 태그를 가지고 id가 god, class 가 foods 인 요소를 리턴
  result.find("li", {'id': 'god', 'class': 'foods'})
  ```

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/BasicWebCrawl/picture/crawl2.png)

---

## 예제
  ### 1. 특정 url 이므로 코드만 아래에...
  - 원하는 것은 `점수`, `이름`, `벌어들인 금액` 을 가져와서 저장 하는 것

  ```python
  import requests
  from bs4 import BeautifulSoup as bs

  response = requests.get("url 주소")
  result = bs(response.text, "html.parser")

  # div 태그에 원하는 값들이 저장되어 있다는 것을 알 수 있으므로 이를 가져옴
  div = result.find('div', {'id': 'homepage-top-box-office'})

  # div 태그 내용 확인하면 table 태그를 가져와야 함을 알 수 있다.
  table = result.find('table', {'id': 'Top-Box-Office'})

  # table 내 tr 태그에 저장되어 있다는 것을 알 수 있으며 이것이 잘 가져와지는지 확인
  for movie in table.find_all('tr'):
      print(movie)
      print("-" * 20)

  # 우리가 필요한 것은
  ## span 태그에서 score 클래스 와 (토마토 점수)
  ## td 태그에서 middle_col 클래스의 a 태그 (이름)
  ## td 태그에서 right_col right 클래스의 a 태그 (벌어들인 금액) => space 가 많으므로 strip 해줌
  for movie in table.find_all('tr'):
      print(movie.find("span",{'class': 'tMeterScore'}).text)
      print(movie.find('td', {'class': 'middle_col'}).find('a').text)
      print(movie.find('td', {'class': 'right_col right'}).find('a').text.strip('\n').strip(' '))
      print("-" * 20)
  ```

  ### 2. 만약 javascript 에 의해서 나중에 호출된다면?
  - 값이 출력이 되지 않는다.
  - 웹페이지가 처음 위에서 requests.get 했을 때 포함하지 않고 있었기 때문 (원하는 정보를 불러오는 자바스크립트 언어가 수행한다는 것을 알 수 있다.)
  - 이는 위와같이 하지 않고 다르게 해야한다. (나주에 배워보자 ㅜㅜ)

  - 예시

  ![](https://github.com/Lee-KyungSeok/Python-Study/blob/master/BasicWebCrawl/picture/crawl3.png)
