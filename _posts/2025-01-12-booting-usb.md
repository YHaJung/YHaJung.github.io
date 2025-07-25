---
title: "부팅 USB 만들기 (feat.  MBR, GPT 선택 기준)"
categories:
- Setting
tags:
- AI
- Deep Learning
- docker
---

본 게시글에서는 아래와 같은 환경을 기준으로 진행하였다.(다른 OS의 부팅 USB를 만들더라도 방법은 딱히 다르지 않다.)

- 설치하고자 하는 OS : Ubuntu 22.04 LTS
- 부팅 USB를 만드는 컴퓨터 : Windows 11
- OS를 설치할 컴퓨터 : 현재 다른 Ubuntu 설치 상태

## OS 설치 파일 다운로드

원하는 OS를 검색하여 설치 이미지를 다운로드 한다.

![image.png](../../assets/images/2025-01-12-booting-usb/image.png)

- 

## Rufus 다운로드

부팅 usb 제작 프로그램인 Rufus를 다운로드한다. 웹에 검색해도 프로그램이 쉽게 나오지만, Windows의 경우 microsoft store에서도 쉽게 다운로드 할 수 있다.

![image.png](../../assets/images/2025-01-12-booting-usb/image%201.png)

## 프로그램 실행 및 설정

프로그램을 다운로드하고 나면, 바로 실행하면 된다. 아래와 같은 프로그램이 나타나면 `선택`을 눌러서, 앞서 다운로드한 우분투 OS 이미지를 선택한다. 이후엔 아래의 선택 기준을 참고하여 `파티션 구성`을 선택하고, `시작` 버튼을 누른다. 

![image.png](../../assets/images/2025-01-12-booting-usb/image%202.png)

- 파티션 구성의 경우 MBR, GPT 2가지 옵션이 있다.
    - MBR은 더 예전부터 사용되던 전통적인 디스크 관리 도구이며, GPT는 이를 대체하기 위해 만든 새로운 디스크 관리 도구이다.
    - 선택은 아래 조건들에 따라 할 수 있다.
        - **하드웨어의 UEFI 지원 여부** - MBR의 경우 UEFI와 BIOS 시스템 모두 사용 가능하고, GPT의 경우엔 UEFI만 지원한다. 보통 2006년 전후로 나뉘는데, 오래된 컴퓨터들의 경우 BIOS만 지원하므로, 이 경우 반드시 MBR을 사용해야 한다. 설치할 컴퓨터의 UEFI 지원 여부는 아래 명령어를 통해 확인할 수 있다.
            
            ```bash
            sudo dmidecode -t bios
            ```
            
            ![image.png](../../assets/images/2025-01-12-booting-usb/image%203.png)
            
        - 설치 운영체제 - 2006년 경 이전의 오래된 운영체제를 설치하고자 하는 경우엔 MBR만 사용 가능하다. Windows 기준으로는 **Windows 7 이하인 경우엔 MBR만 사용 가능하고, 이후로는 둘 다 사용 가능**하다.
        - 하드 디스크의 용량 - MBR의 경우 단일 파티션의 용량이 2TB일 때까지만 설치할 수 있다. 따라서 **더 큰 디스크에 설치하고자 할 때에는 GPT만 사용할 수 있고, 2TB 이하라면 둘 다 사용할 수 있다**. 사용할 컴퓨터의 하드 디스크나 파티션 용량을 모를 경우, 아래 명령어를 통해 확인할 수 있다.
            
            ```bash
            df -h
            
            # 만약 \dev\loop 등 자잘한 저장공간이 많이 떠서 파악이 어렵다면 아래 명령어를 사용한다.
            # df -h -x squashfs -x tmpfs
            ```
            
        - 파티션의 수 - **하나의 디스크에 4개가 넘는 파티션을 만들고자 할 경우엔 GPT를 사용하여야 한다**. MBR의 경우 파티션을 4개까지만 만들 수 있고, GPT의 경우엔 최대 128개의 기본 파티션과 무제한의 논리 파티션을 지원한다.
        - 듀얼 부팅 - **듀얼 부팅** 용으로 만들고자 할 경우엔, 다른 쪽 OS와 파티션 구성 방식을 **통일시켜야 한다.**
    - 둘 다 가능할 때
        
        필자의 경우, UEFI를 지원하는 컴퓨터, Ubuntu 22.04 LTS로 오래되지 않은 운영체제이고, 하드 디스크 총 용량은 2TB, 파티션은 아직 나눌 계획이 없음, 듀얼 부팅 안 함. 이 조건으로 인해서 두 가지 방식 모두 사용할 수 있었다. 앞으로도 듀얼 부팅을 하더라도 Window 7 이전의 오래된 OS를 사용할 일은 없을 것 같아서, 최신 버전이라 속도나 보안성이 높은 **GPT를 선택**하였다. (하지만 이는 사람에 따라 선호하는 것이 다르다. 다른 이유가 없다면 호환성이 더 높은 MBR을 선택하는 것이 좋다는 의견도 많다.)
        

## 부팅 USB 만들기 진행

아래와 같이 차례로 확인 버튼을 누르면 부팅 USB가 완성된다.

![image.png](../../assets/images/2025-01-12-booting-usb/image%204.png)

![image.png](../../assets/images/2025-01-12-booting-usb/image%205.png)

![image.png](../../assets/images/2025-01-12-booting-usb/image%206.png)

## 완료

아래와 같이 `준비`라고 뜨면 부팅 USB 제작이 완료된 것이다. 프로그램을 닫으면 된다.

![image.png](../../assets/images/2025-01-12-booting-usb/image%207.png)

## 참고자료

- [https://cprogramming.tistory.com/entry/Ubuntu-USB](https://cprogramming.tistory.com/entry/Ubuntu-USB)
- [https://www.easeus.co.kr/partition-manager-software/mbr-or-gpt-for-ssd.html](https://www.easeus.co.kr/partition-manager-software/mbr-or-gpt-for-ssd.html)