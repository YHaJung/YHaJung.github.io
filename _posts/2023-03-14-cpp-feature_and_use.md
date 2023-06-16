---
title : "[C++] C++의 특징 및 사용법"
categories:
- c++
tags:
- c++
---

## 장단점

|  | C/C++ | Python |
| --- | --- | --- |
| 특징 | Compile 언어 | Interpreter |
| 장점 | - Controllability : 메모리 최적화 가능 <br> - 빠름 | - 자동화 잘 되어있음 <br> - debugging 및 prototyping에 유리 <br> - ML용 lib 많음 |
| 단점 | - 배우기 어려움 <br> - 유연성이 낮음(전체에 하나의 error라도 있으면, 실행 자체가  안됨) <br> - ML용 lib 적음 | - 메모리 최적화 힘듦 <br> - 느림 |

- python으로 prototyping 후에 C/C++로 바꾸어 속도를 올려 쓰는 식으로 섞어 쓰기 좋다.
- python의 library들이 c/c++로 작성되어 있는 경우 많다. → 코드 내부 이해를 위해 c/c++ 읽을 줄 알아야 함.

## 사용법

- prerequirements
    - gcc
    - vscode, vscode 확장자 c/c++
    - git, vscode git bash
- 파일 생성
    - 파일명.cpp 로 파일 만들기
- 컴파일
    
    ```bash
    # c comfile
    gcc 파일명.c -o exe파일명 # exe파일명 뒤에 확장자(.exe)는 붙여도 되고, 안 붙여도 됨
    
    # cpp confile
    g++ 파일명.cpp -o exe파일명 # exe파일명 뒤에 확장자(.exe)는 붙여도 되고, 안 붙여도 됨
    
    # cpp 파일 여러개 compile
    g++ -std=c++11 -o bear main.cpp bear.cpp mommabear.cpp
    ```
    
- 실행
    
    ```bash
    ./exe파일명
    ```