---
title : "git remote repository 설정/바꾸기"
categories :
    - 사용법
tags :
    - git
---


- 현재 git remote로 설정된 repository 확인하기
```bash
git remote -v
```

- remote repository 설정
    - 기존 remote repository가 없을 경우, 아래 명령어로 remote repository를 설정한다.
    
    ```bash
    	git remote add origin https://github.com/{목표주소}.git
    ```
    

- remote repository 변경
    - 기존 remote repository가 있지만, 다른 주소로 바꾸고 싶을 경우 아래 명령어를 사용한다.
    
    ```bash
    git remote set-url origin https://github.com/{목표주소}.git
    ```
    

### 참고자료

- [https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)