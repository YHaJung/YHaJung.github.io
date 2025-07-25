---
title: "[Debug] Ubuntu 18.04 설치 시 Black Screen 해결"
categories:
- Debug
tags:
- Ubuntu
---

## 해결방법

1. 전원버튼을 누른 후 shift를 누르고 있으면 grub로 진입 후 recovery mode로 boot할 수 있다.
2. 맨 위의 항목인 Resume normal boot를 들어가면 그래픽드라이버없이도 ui에 접근 가능하다.
3. 다음의 세 명령을 실행 한다.
    1. sudo apt-get update
    2. sudo apt-get upgrade
    3. sudo ubuntu-drivers autoinstall
4. 재부팅 후 정상적으로 ubuntu ui에 접근하는 것을 확인할 수 있다.

## 참고자료

- [https://hpkim0512.blogspot.com/2019/09/ubuntu-1804.html?m=1](https://hpkim0512.blogspot.com/2019/09/ubuntu-1804.html?m=1)