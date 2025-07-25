---
title: "[Setting] WSL2 설치 : 윈도우 용 Linux 시스템 (Window 11)"
categories:
- Setting
tags:
- Linux
- WSL
- Windows
---

이 글은 Window 11을 기준으로 작성되었다. Windows 10 버전 2004 이상(빌드 19041 이상) 또는 Windows 11이 아닌 경우에는 [수동 설치 방법](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual)을 참고하기 바란다.

- WSL이란 `Linux용 Windows 하위 시스템` 으로 Window 노트북에서 리눅스 환경을 사용하게 해주는 기능이다.
- WSL 1보다 2가 훨씬 다양한 기능이 있으며, 대부분의 경우 2의 기능을 필요로 한다. 따라서 특별한 이유가 없다면 2를 설치할 것을 강하게 권장한다.

## 1. 관리자모드로 Power Shell 열기

power shell을 검색 후 우클릭해서 `관리자로 실행` 을 누른다.

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled.png)

## 2. wsl 설치

- 기본 Ubuntu로 설치
    
    원하는 리눅스 설정 없이 기본 wsl만 설치하려면 아래 명령어를 입력한다.
    
    ```bash
    wsl --install
    ```
    
- 리눅스 배포판 지정 설치
    
    원하는 리눅스 배포판으로 지정하여 설치하려면 아래 명령어를 사용한다.
    
    차후 ubuntu 배포판이 어차피 필요하므로 이때 한 번에 설정해서 설치하는 것이 더 편리하다.
    
    ```bash
    wsl --list --online # 설치 가능한 ubuntu 배포판 확인
    wsl --install -d <설치하려는리눅스이름> # ubuntu 배포판 설치. 예) wsl --install -d Ubuntu-20.04
    ```
    

## 3. 다시 시작 & 기본 설정

- 설치가 끝나면 다시 시작한다.
- 다시 시작하면 자동으로 ubuntu terminal이 열리고, username과 password를 설정하는 부분이 뜬다. 원하는 대로 설정해준다.

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%201.png)

## 4. 설치 확인

- ubuntu terminal 대신 다른 창 (power shell)을 열어서, 아래 명령어를 입력해주면 설치된 wsl 버전과 리눅스를 확인할 수 있다.

```bash
wsl -l -v # 설치된 wsl 버전 확인
```

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%202.png)

- 이제 사용 가능한 터미널에 리눅스 환경이 추가되었음을 확인할 수 있다.

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%203.png)

- 터미널에서 새 창을 열 때 기본 설정을 wsl로 하고 싶은 경우, 설정으로 들어가서 `시작`- `기본 프로필`을 변경 후 저장한다.

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%204.png)

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%205.png)

## (참고) 기타 wsl 명령어

- 위와 같은 방법으로 설치할 경우, 자동으로 wsl2와 원하는 지정한 리눅스 버전으로 설정되므로 아래 명령어 들을 추가로 입력할 필요는 없다.
- 원하는 것과 다르게 설치한 경우에는 아래 명령어를 참고한다.

```bash
wsl --set-default-version 2 # wsl 버전을 2로 변경
wsl --list --verbose # 설치된 ubuntu 배포판 (디폴트 설정에 * 표시)
wsl --list --online # 설치 가능한 ubuntu 배포판
wsl --install -d <설치하려는리눅스이름> # ubuntu 배포판 설치
wsl --set-default 리눅스배포판이름 # 디폴트 리눅스 배포판 설정
```

## (옵션) VS Code에서 WSL 사용하기

- WSL 확장자를 설치한다.

![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%206.png)

- VS Code의 기본 터미널을 WSL로 설정하기
    - 왼쪽 톱니바퀴 - 설정 - features - terminal 에서 설정을 `wsl.exe`로 바꾼다.
    
    ![Untitled](../../assets/images/2024-12-25-wsl2-install/Untitled%207.png)
    

## (추가) GPU 사용 설정

- Window에 리눅스 환경을 설치하는 경우는 AI 등 개발 목적이 많을 것이다. 이를 위해 GPU 사용이 필요할 경우, WSL GPU 사용 세팅 게시글을 참고하길 바란다.

## 참고자료

- Linux용 Windows 하위 시스템
- https://velog.io/@dragoocho/컴퓨터-환경셋팅-WSL-2-기본터미널-설정
- [https://wonderbout.tistory.com/211](https://wonderbout.tistory.com/211)