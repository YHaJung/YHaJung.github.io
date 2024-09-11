---
title: "FileZilla 설치 및 사용법 : 원격 컴퓨터에 쉽게 파일 전송하기"
categories:
- Setting
tags:
- FileZilla
- Data
- Remote
- SSH
---


FileZilla라는 프로그램을 이용하면, 쉽게 원격 컴퓨터와 데이터를 주고 받을 수 있다.

## 프로그램 설치

필요하면 양쪽 컴퓨터에 모두 설치해도 되지만, 양방향으로 데이터를 보낼 수 있는 프로그램이므로 로컬 컴퓨터에만 설치하면 된다.

설치 파일은 [FileZilla 홈페이지](https://filezilla-project.org/)에서 쉽게 다운로드 할 수 있다.

아래 페이지에서 ZileZilla Client를 다운로드해서 실행해주면 끝이다.

![image.png](../../assets/images/2024-09-11-filezilla/image.png)

설치가 끝나고 프로그램을 실행해보면 아래와 같은 화면이 나타난다.

![image.png](../../assets/images/2024-09-11-filezilla/image%201.png)

## 서버 연결하기

간단한 일회성 연결은 아래의 한 줄만 간단히 입력해주면 된다.

호스트는 `sftp://ip주소` 구조로 입력하고, 포트번호는 ssh 기본 포트인 22인 경우 입력하지 않아도 된다.

![image.png](../../assets/images/2024-09-11-filezilla/image%202.png)

## 자주 연결할 사이트 설정 (사이트 관리자)

한 번만 연결하고 말 것이 아니라, 자주 파일이 오고 갈 사이트의 경우, `사이트 관리자`에 등록해 두는 것이 편하다.

![image.png](../../assets/images/2024-09-11-filezilla/image%203.png)

![image.png](../../assets/images/2024-09-11-filezilla/image%204.png)

![image.png](../../assets/images/2024-09-11-filezilla/image%205.png)

사이트 이름은 기억하지 좋은 이름으로 설정한다.

프로토콜은 일반적인 경우 `SFTP`로 사용하는 것이 안정적이다.

호스트에는 ip주소를 입력해주면 된다.

그 외의 포트, 사용자, 비밀번호를 입력하고, `연결` 혹은 `확인` 을 눌러 저장해주면 된다.

이후로는 사이트 관리자에 들어와 원하는 사이트를 선택하고 연결 버튼을 누르는 것으로 간단하게 해당 사이트로 연결할 수 있게 된다.