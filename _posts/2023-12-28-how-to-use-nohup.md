---
title : "nohup을 이용한 백그라운드 실행법"
categories:
    - 사용법
tags:
    - bash
---


### 요약

```bash
#nohup 명령어 -u 실행파일 > 출력파일경로.out &
nohup python -u train.py > log/train01.out &
```

### 사용 시 장점

- 백그라운 실행 → 컴퓨터나 창을 종료해도 계속 코드 작동
- 실행 로그 저장 : 프로그램 출력이 nohup.out 파일에 지속적으로 기록
    - 중간에 에러 등으로 종료되어도 기록이 남음
    - 컴퓨터를 껐다가 켜도 로그 확인 가능
    - 다른 명령을 수령하고 나서도 이전 기록 누적 확인 가능
    - 실행 중간에도 계속 update됨

### 기본 사용법

- 사용할 명령어 앞엔 `nohup`, 뒤엔 `&`을 붙인다.
- 현재 경로에 `nohup.out` 파일이 생성되며 출력이 기록된다.
- 예시
    
    ```bash
    nohup python main.py --lr=0.5 &
    ```
    

### 즉시 출력

- nohup 사용 시, 출력이 실시간으로 안 찍히고 나중에 몰아서 나오는 경우가 자주 발생한다. 이를 해결하기 위해선 아래 코드를 사용한다.
    
    ```bash
    nohup python -u train.py &
    ```
    
- shell 파일을 사용할 경우, sh -u xx.sh가 아닌 파일 속 python 명령어에 -u를 입력하여야 한다.

### 출력 파일 명 설정

- & 전에 `> 파일명`을 추가한다.
- 예시
    
    ```bash
    nohup python train.py > train01.out &
    ```
    
- 경로도 지정 가능하다.
    
    ```bash
    nohup python train.py > ../logs/train02.out &
    ```
    

### 강제 종료

- 코드 실행이 종료되면 프로세스는 자동 종료된다. 하지만 중간에 실행을 중단하고 싶을 때가 있다. 그럴 땐 직접 프로세스를 중단시켜야한다.
- 현재 실행 중인 프로세스들을 확인한다.
- 예시
    
    ```bash
    ps auxf | grep 작성자아이디
    ```
    
    ```bash
    ps -ef | grep 실행파일명
    ```
    

- 프로세스를 종료시킨다.
- 예시
    
    ```bash
    kill -9 프로세스ID
    ```