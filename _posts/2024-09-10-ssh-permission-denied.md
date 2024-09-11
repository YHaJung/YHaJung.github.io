---
title: "[Debug] ssh -  permission denied, please try again"
categories:
- Debug
tags:
- Debug
- Remote
- SSH
---


ssh 연결을 위해서 아래와 같은 명령어로 접속하고자 했을 때 나타나는 에러이다.

```bash
ssh user계정@ip주소
```

위와 같이 입력하면 password를 물어보게 되는데, 정상적인 경우엔 그 password가 틀렸을 때 나타나는 에러이다.

따라서 처음 이런 에러를 보면, 우선 비밀번호가 확실히 맞는지 체크하는 것이 우선이다.

하지만 때로 분명 비밀번호를 정상적으로 입력하였는데도 반복적으로 Permission denied 에러가 나타날 때가 있다.

이런 경우에 문제를 해결한 과정을 소개한다.

## Server의 PasswordAuthentication 설정 확인

가장 일반적인 해결책은 원격 컴퓨터의 sshd 설정을 변경하는 것이다.

1. sshd_config 수정

```bash
vim /etc/ssh/sshd_config
```

파일의 `PasswordAuthentication` 부분이 no로 되어있다면 `yes`로 변경

1. sshd system 재시작

```bash
systemctl restart sshd
```

## OpenSSH Client 재설치

하지만 필자의 경우 위의 방식으로 해결되지 않았다.

이때 발견한 특이한 점은 Putty에서는 동일한 설정으로 정상적으로 ssh 접속이 되고, cmd 등 터미널에서 입력할 때는 위와 같은 에러가 발생하고 있다는 것이었다.

이에서 알 수 있는 점은 서버 설정의 문제가 아니라, OpenSSH 클라이언트 쪽에 문제가 있다는 것이다.  PuTTY는 기본적으로 `.ppk` 형식의 SSH 키를 사용하지만, CMD에서는 OpenSSH를 통해서 `.pem` 형식의 키를 사용하기 때문이다.

이와 관련에서 찾아본 결과, 아래 방식으로 해결할 수 있었다.

1. (윈도우 컴퓨터 기준으로) `설정` - `시스템` - `선택적 기능` 에서 OpenSSh Client를 찾아서 삭제한다.

![image.png](../../assets/images/2024-09-10-ssh-permission-denied/image.png)

1. 컴퓨터 재시작(Reboot)
2. 선택적 기능 추가에서 다시 설치해준다.
    
    ![image.png](../../assets/images/2024-09-10-ssh-permission-denied/image%201.png)
    
3. 컴퓨터 재시작(Reboot)

## 참고자료

- [https://honeywater97.tistory.com/122](https://honeywater97.tistory.com/122)
- [https://chatgpt.com/c/66de8873-2a50-8005-96c2-b9f347bae868](https://chatgpt.com/c/66de8873-2a50-8005-96c2-b9f347bae868)