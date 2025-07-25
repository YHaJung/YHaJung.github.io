---
title: "Ubuntu 설치 및 필수 세팅 (Ubuntu 22.04 LTS)"
categories:
- Setting
tags:
- Ubuntu
- 부팅USB
- 설치
- 우분투
---

아직 우분투가 설치되지 않은 상태에서는 화면 캡쳐가 안되기 때문에 관련된 부분은 예시 화면 그림이 존재하지 않는다.

하지만 복잡한 선택이 존재하지 않기 때문에 설명을 잘 읽고 따라하면 그대로 진행할 수 있다.

## 부팅 USB로 컴퓨터 시작

부팅  USB를 꽂고 컴퓨터를 시작한다. (부팅 USB가 없다면 [부팅 USH 만들기](%E1%84%87%E1%85%AE%E1%84%90%E1%85%B5%E1%86%BC%20USB%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5%20(feat%20MBR,%20GPT%20%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%20%E1%84%80%E1%85%B5%E1%84%8C%E1%85%AE%E1%86%AB)%20f5093d606aa54abc9362461c691c111f.md) 글을 참고하여 만든다.)

## Boot Device 세팅

이때 이미 설치되어있는 다른 OS가 있을 경우엔 부팅 USB로 접근하기 위해 Boot Device 세팅 모드로 들어가야 한다. 

빈 컴퓨터에 설치하는 경우엔 이 단계는 건너 뛰어도 자동으로 부팅 USB로 접근된다.

- Boot Device 설정 모드로 들어가기
    
    컴퓨터를 켜는 도중에 뜨는 검은 창 혹은 제조사 마크가 뜨는 화면에서 제조사에 따라 `F2`, `F12`, `DEL` 등의 키 중 하나를 계속 연타한다. 제조사에 따라 어떤 키를 연타하면 되는지는 [제조사 별 BIOS 모드 혹은 부팅 디바이스 설정](%E1%84%8C%E1%85%A6%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A1%E1%84%87%E1%85%A7%E1%86%AF%20Bios%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%B3,%20%E1%84%87%E1%85%AE%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A9%E1%84%83%E1%85%B3%20%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(+%20%E1%84%86%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%87%20c31439bf1f4a41cb8c825165bfc09804.md) 포스팅을 참고한다.
    
    필자의 경우 DELL 메인보드를 사용하는 컴퓨터라 `F12`를 연타하였다.
    
- 디바이스 설정
    
    디바이스 설정 창이 나타나면, Boot Devices 리스트에서 부팅 USB를 선택한다.
    
    필자의 경우 필자의 경우 `UEFI SanDisk Cruzer Blade` 를 선택하였다.
    
- 검은 화면에서 `Try or Install Ubuntu` 선택
    
    부팅 USB를 선택하고 계속 진행하면, 검은 화면에서 부팅 방식을 묻는다. `Try or Install Ubuntu`를 선택한다.
    

## 우분투 Ubuntu 설치하기

우분투 화면이 Install 켜지고, 창이 뜬다. 설명을 읽으며 차례로 진행하면 된다.

- Welcome : `English` - `Install Ubuntu` 선택
    
    한국인이어도 English 선택을 권장한다. 설명문이 한국어로 나오면 정확도도 떨어지고 검색해도 잘 안 나와서 디버깅이 매우 힘들다.
    
- Keyboard Layout : `English (US)` - `English (US)`
    
    위에서와 마찬가지로 English를 선택한다.
    
- Wireless : 와이파이 연결
    
    스킵하지 말고 해주자. 설치 과정에서 인터넷이 안 돼서 건너뛰는 게 있으면, 나중에 귀찮아질 수 있다.
    
- Updates and other software : `Normal Installation` - `Download updates while installing Ubuntu` 체크
    
    별 다른 필요가 없으면 추천대로 위 버튼대로 설정하고 continue한다.
    
- Installation type : 원하는대로
    
    이건 딱히 정답이 없다. 설명문 읽어보고 원하는대로 설치한다. 기존 OS를 유지하고 듀얼 부팅을 하고 싶으면 Install Ubuntu alongside with ~, 기존 OS만 지우고 새로 깔고 싶으면 Erase Ubuntu and reinstall, 디스크 다 지우고 새로 깔려면 `Erase disk and install Ubuntu` (필자는 이걸 선택), 파티션을 설정하고 싶은 형태가 있으면 Something else이다.
    
- Where are you? : Seoul
    
    보통 자동으로 뜨니 그냥 넘기면 된다.
    
- Who are you?
    
    컴퓨터에서 사용하고 싶은 이름, 컴퓨터이름, 암호를 설정하고 continue.
    
    모두 영어로 쓰기를 권장한다. 개발할 때 (특히 리눅스에서) 한글 쓰지 말자. 시스템 불안정해진다.
    

이제 설치 완료를 기다린다.

창이 뜨면 Reinstall Now를 누르고 기다리면, Ubuntu로 재시작 된다.

이러면 기본적인 설치는 끝났다.

## 기본 업데이트

처음 시작되면 창이 하나 뜨고, 정보를 보내겠냐, 위치 접근을 허락하겠냐 등등 물어본다. 굳이 필요 없기도 하고 privacy도 신경 쓰여서 전부 `skip for now` 혹은 `do not send` 등을 선택하고 done을 눌러 껐다.

- Software Updater : `Install Now` - `Restart Now`
    
    조금 있다 보면 Software Updater가 뜬다. 이건 결국 필요한 기능들이고, 반복해서 물어보므로 `Install Now`를 선택해서 설치한다.
    
    ![Screenshot from 2024-09-06 16-15-22.png](../../assets/images/2024-10-18-ubutnu-install-and-settings/Screenshot_from_2024-09-06_16-15-22.png)
    
    설치가 끝나면 재시작 할지 묻는 창이 나타난다. 안정적인 사용을 위해 `Restart Now`를 눌러준다.
    
    ![Screenshot from 2024-09-06 16-25-39.png](../../assets/images/2024-10-18-ubutnu-install-and-settings/Screenshot_from_2024-09-06_16-25-39.png)
    

## 한글 사용 설정

기본 설정은 영어로 해서 설치하기를 권장하지만, 그렇다고 한글 사용이 안되는 것은 곤란하다.. 한글로 된 코드 주석이 제대로 표시되지도 않을 것이고, 검색도 제대로 하기 힘들며, 하다 못해 메모도 불편하다.

따라서 우분투 설치가 끝나면 한글 사용을 위한 기본적인 설정을 해주는 것이 좋다.

한글 설치는 [Ubuntu 한글 사용 설정](Ubuntu%2022%2004%20%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%B3%E1%86%AF%20%E1%84%8F%E1%85%B5%E1%84%87%E1%85%A9%E1%84%83%E1%85%B3%20%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%208b7a5c1d24bf4b828fe050934dc76772.md) 글을 참고하면 된다.(다소 복잡한 과정을 필요로 한다.)