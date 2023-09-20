--- 
title : "Window 파일탐색기에서 원격 서버 폴더 사용(SFTP)"
categories:
- Setting
tags:
- setting
- window
- remote
---

## 1. 설치 필요 파일

- https://github.com/winfsp/winfsp
- https://github.com/winfsp/sshfs-win

## 2. 설정

- 파일탐색기의 `내 pc`에서 `네트워크 드라이브 연결` 로 들어간다.
    
    ![Untitled](../../assets/images/2023-09-13-sftp-window-remote-folder/Untitled.png)
    
- `\\sshfs\username@ip주소` 형식으로 입력한다.
    - 필요할 경우 port `!포트번호` 도 추가한다.
    
    ![Untitled](../../assets/images/2023-09-13-sftp-window-remote-folder/Untitled%201.png)
    

## 3. 완료

- 내 pc로 들어가면 추가된 네트워크를 확인할 수 있다.
    ![Untitled](../../assets/images/2023-09-13-sftp-window-remote-folder/Untitled%202.png)