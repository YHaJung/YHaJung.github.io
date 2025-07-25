---
title: "내 우분투 컴퓨터에 ssh로 원격접속"
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
    apt list openssh*
    ```
    
    `openss-client`와 `openssh-server`에 `[installed]`가 붙어있으면 설치되어 있는 것이다.
    
    ![Untitled](../../assets/images/2025-01-10-ubuntu-ssh-server/Untitled.png)
    
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
    
    ![Untitled](../../assets/images/2025-01-10-ubuntu-ssh-server/Untitled%201.png)
    
    - 만약 `Unit sshd.service could not be found.`와 같은 에러가 나타나면, 다음을 실행해준다.
        - [https://hmw0908.tistory.com/116](https://hmw0908.tistory.com/116)
    
    ```bash
    ss -nlt
    ```
    
    ssh가 사용하는 22번 포트의 state가 LISTEN인지 확인한다.
    
    ![Untitled](../../assets/images/2025-01-10-ubuntu-ssh-server/Untitled%202.png)
    

### 방화벽 허용

방화벽이 막혀있으면 작동이 안될 수 있다. 방화벽 허용 여부를 확인한다.

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
    
    ![Untitled](../../assets/images/2025-01-10-ubuntu-ssh-server/Untitled%203.png)
    

## ssh 접속 테스트

- Putty 설치 및 사용
    
    putty를 설치하여 실행한다. 윈도우의 경우 microsoft store에서 쉽게 설치할 수 있고, 인터넷 브라우저에 검색해서 설치도 가능하다.
    
    ![image.png](../../assets/images/2025-01-10-ubuntu-ssh-server/image.png)
    
- Putty에 IP 주소를 입력하고, Open을 선택한다.

![image.png](../../assets/images/2025-01-10-ubuntu-ssh-server/image%201.png)

- 창이 열리면, 연결할 계정과 비밀번호를 입력한다.

![image.png](../../assets/images/2025-01-10-ubuntu-ssh-server/image%202.png)

- 단순 ssh 연결만 할 경우, 사실 굳이 putty를 설치할 필요없이 cmd 등 terminal에 아래 명령어를 입력해서 연결할 수 있다. 하지만 유무선을 포함한 여러 네트워크를 사용하는 등 복잡한 환경에서는 terminal 명령어 만으로는 에러를 낼 수 있다. 따라서 설정 확인을 위해선 우선 putty로 먼저 해보는 것이 편리하다. 이후 필요한 환경에서 문제가 없으면 사용하면 된다.
    
    ```bash
    ssh 계정이름@ip주소
    ```
    

## 참고자료

- [https://velog.io/@717lumos/Ubuntu-SSH로-원격접속-하기](https://velog.io/@717lumos/Ubuntu-SSH%EB%A1%9C-%EC%9B%90%EA%B2%A9%EC%A0%91%EC%86%8D-%ED%95%98%EA%B8%B0)