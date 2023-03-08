---
title: "내 우분투 컴퓨터에 ssh로 원격접속하기"
categories:
  - 사용법
tags:
  - ubuntu
  - 원격접속
---

내 컴퓨터의 리소스를 사용하기 위해, 원격을 다른 컴퓨터에서 접속하고 싶을 수 있다.

ssh를 통해 간단히 접근하기 위한 설정법을 알아보자

## 원격 컴퓨터 설정

### 네트워크에 연결되어 있어야 한다.

### IP 주소 확인

```bash
ifconfig
```

inet addr: 뒤에 오는 000.000.0.000 형식의 숫자이다. 이 숫자를 기억해두자.

### sshd 서버

- 설치 여부 확인

```bash
sudo apt list openssh*
```

`openss-client`와 `openssh-server`에 `[installed]`가 붙어있으면 설치되어 있는 것이다.

![image](https://user-images.githubusercontent.com/49065638/199444505-766cb5a8-51a8-4b36-a98a-dbc522843cea.png)


- 설치하기

설치되어 있지 않으면 직접 설치해준다.

```bash
sudo apt install openssh-server
```

- 서비스 실행 확인하기

```bash
systemctl status sshd
```

`active(running)`으로 표시되면 실행 중인 것이다.

![image](https://user-images.githubusercontent.com/49065638/199445073-c6b7d22b-900f-4716-bb1c-e04d3318ada8.png)

```bash
ss -nlt
```

ssh가 사용하는 22번 포트의 state가 LISTEN인지 확인한다.

![image](https://user-images.githubusercontent.com/49065638/199445399-e8bc892e-fcd7-49ae-a8bb-0a4d8b3e24a5.png)

### 방화벽 허용

방화벽이 막혀있으면 작동이 안될 수 있다. 방화벽 허용 여부를 확인한다.

```bash
iptables -nL
```

- 방화벽 상태와 허용 여부 확인

```bash
sudo ufw status
# sudo apt install ufw # ufw가 없다면 설치
```

- 방화벽 활성화

```bash
sudo ufw enable
sudo ufw allow 22/tcp
```

![image](https://user-images.githubusercontent.com/49065638/199445557-a39ca3f1-1284-4d0e-9999-75655158efcd.png)

## ssh 접속

```bash
ssh 계정이름@ip주소
```

## 참고자료

- [https://velog.io/@717lumos/Ubuntu-SSH로-원격접속-하기](https://velog.io/@717lumos/Ubuntu-SSH%EB%A1%9C-%EC%9B%90%EA%B2%A9%EC%A0%91%EC%86%8D-%ED%95%98%EA%B8%B0)