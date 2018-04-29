# 파이썬 가상환경
  - 파이썬 가상환경 설정

---

## 파이썬 가상환경 (python virtual environment)
  ### 1. 파이썬 가상환경이란?
  - 컴퓨터 내 특정 공간 내에 공간 전용의 파이썬을 설치
  - 각각의 프로그램마다 환경 분리 가능
  - 사용이유
    - 버전의 분리 (버전과의 통일성을 위해)
    - 서버와의 통일 ()

  ### 2. 파이썬 가상환경 생성 및 실행
  - 가상환경 생성

  ```bash
  # Mac
  python3 -m venv [가상환경이름]
  # Window
  python -m venv [가상환경이름]
  ```

  ### 3. 파이썬 가상환경 실행
  - 가상환경 실행

  ```bash
  # Mac
  source [가상환경폴더]/bin/activate
  # Window
  .\\[가상환경폴더]\\Scripts\\activate
  ```

  ### 4. 가상황경 종료
  - 가상환경 종료

  ```bash
  deactivate
  ```

  ### 5. 특정 프로그램 설치하기
  - 장고 : `pip install django`
  - 텐서플로우 : `pip install --upgrade tensorflow`
  - 텐서플로우(GPU) : `pip install --upgrade tensorflow-gpu`

---
## 참고
  ### 1. 파이썬 설치 경로 확인
  - 파이썬이 설치된 경로 확인

  ```bash
  # Mac
  which python3
  # Window
  get-command python
  ```

  ### 2. 설치된 라이브러리 확인
  - 라이브러리 확인

  ```bash
  # Mac
  pip list
  # Window
  pip3 list
  ```

  ### 3. pyenv
  - pyenv는 파이썬에 대한 버전관리를 할 수 있도록 해준다.
  - 단> window 는 지원하지 않는다. ([참고](https://github.com/Lee-KyungSeok/Linux-Study/tree/master/Python))

  ### 4. 윈도우 보안 에러 해결방법
  - 관리자 모드 실행
  - `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned` 명령어 입력 후 `Y` or `A` 입력
