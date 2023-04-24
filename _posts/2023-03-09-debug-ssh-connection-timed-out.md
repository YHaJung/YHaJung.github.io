---
title : "[Debug] ssh: connect to host ~ port 22: Connection timed out"
categories:
- setting
tags:
- setting
- debug
---


- 일반적으로 위와 같은 에러는 server 컴퓨터에 ssh관련  툴 설치가 안 되어있거나 방화벽이 막혀있을 때 나타난다.
    - 이 경우 ****[내 우분투 컴퓨터에 ssh로 원격접속하기](https://yhajung.github.io/%EC%82%AC%EC%9A%A9%EB%B2%95/access-my-remote-ubuntu-with-ssh/)** 를 참고하면 된다.

- 하지만 필자의 경우 위의 것을 모두 다시 하여도 문제가 해결되지 않았다.
- 온갖 서칭을 다 해본 결과 알게 된 것은 집에 있는 와이파이 공유기가 연결을 차단하고 있다는 것이었다…
- sk 통신사의 와이파이의 경우 Port 22를 차단하는 경우가 종종 있다고 한다.

## Server 컴퓨터의 ssh port 번호 바꾸기

- ssh configuration file을 편집한다.

```bash
sudo vi /etc/ssh/sshd_config
```

이 중 Port 22라고 표시된 부분을 원하는 포트 번호로 바꾸고 파일을 저장한다.

- 1024 ~65536의 숫자여야 한다고 한다.
- 필자는 임의로 Port 22220으로 바꾸었다.

![image](https://user-images.githubusercontent.com/49065638/233907948-d6cdfb7c-bdc4-455b-acf2-1b236da2364b.png)

- ssh를 재시작한다.

```bash
service ssh restart




```

- 바꾼 포트번호를 인식하고 있는지 확인한다.

```bash
ss -nlt
```

![image](https://user-images.githubusercontent.com/49065638/233907963-34b8b952-2ec8-447d-b12e-0be6b9dc6f70.png)

- 새로운 포트번호를 **방화벽 허용**한다.

```bash
sudo ufw allow 22/tcp
sudo ufw status
```

![image](https://user-images.githubusercontent.com/49065638/233907984-dbdf193b-b69b-441b-8c94-12ec72cc10bf.png)

## 참고자료

- [https://www.ionos.com/help/server-cloud-infrastructure/getting-started/important-security-information-for-your-server/changing-the-default-ssh-port/](https://www.ionos.com/help/server-cloud-infrastructure/getting-started/important-security-information-for-your-server/changing-the-default-ssh-port/)
- [https://yhajung.github.io/사용법/access-my-remote-ubuntu-with-ssh/](https://yhajung.github.io/%EC%82%AC%EC%9A%A9%EB%B2%95/access-my-remote-ubuntu-with-ssh/)