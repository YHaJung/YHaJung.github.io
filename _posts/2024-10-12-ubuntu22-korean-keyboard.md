---
title: "Ubuntu 22.04 한글 키보드 사용하기"
categories:
- Setting
tags:
- Ubuntu
- 우분투
---

## 1. 한국어 언어팩 다운로드

이 단계는 지역을 한국으로 인식한 상태에서, 우분투 설치 후 이미 조금 사용을 하면서 리부트 몇 번을 한 경우엔 이미 설치되어 있을 가능성이 높다.

하지만 방금 막 우분투를 설치하고, 바로 한글 사용 설정을 하려하는 경우엔 아직 언어팩이 제대로 다운로드 되지 않았을 가능성이 높다. 지역을 한국(서울)로 설정하지 않았다면 더더욱 한국어 언어팩은 설치되어 있지 않을 것이다.

이 경우엔 아래 절차대로 언어팩을 다운로드 해 준다.

- `Setting` - `Region & Language` - `Manage Installed Languages` 를 선택한다.
    
    ![Screenshot from 2024-09-06 17-31-51.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-31-51.png)
    
    - 지역을 한국으로 설정되어 있는 경우엔, 이를 선택하면 아래와 같이 언어가 아직 제대로 설치되지 않았다는 안내 문구가 뜰 것이다. 이땐 바로 `Install`을 눌러 설치해주면 된다.
        
        ![Screenshot from 2024-09-06 17-29-09.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-29-09.png)
        
    - 만약 지역을 한국으로 하지 않은 등의 이유로 안내 문구가 뜨지 않을 경우에는 `Install / Remove Language`를 선택하여, `Korean`에 체크하여 `Apply` 하면 된다.
        
        ![Screenshot from 2024-09-06 17-42-51.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-42-51.png)
        
- 위 과정이 끝나고 나면, 언어 메뉴를 내려보면 한국어를 확인할 수 있다. 이를 확인하고 나면, 꼭! `Reboot` 한다. 그래야 다운로드한 내용이 적용된다.
    
    ![Screenshot from 2024-09-06 17-31-23.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-31-23.png)
    

## iBus 한글 input 추가

- Terminal을 열고 아래 명령어를 입력한다.
    
    ```bash
    ibus-setup
    ```
    
- 창이 뜨면 `Input Method` 의 `Add`를 눌러서 `Korean`  - `Hangul` 을 추가해준다.
    
    이때 반드시 Hangul이어야 하며, 다른 Korean을 선택하면 안된다. 만약 Hangul이 보이지 않는다면 위의 [1.  한국어 언어팩 다운로드](Ubuntu%2022%2004%20%E1%84%92%E1%85%A1%E1%86%AB%E1%84%80%E1%85%B3%E1%86%AF%20%E1%84%8F%E1%85%B5%E1%84%87%E1%85%A9%E1%84%83%E1%85%B3%20%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%208b7a5c1d24bf4b828fe050934dc76772.md) 부분이 제대로 수행되지 않은 것이니, 다시 점검이 필요하다.
    
    ![Screenshot from 2024-09-06 17-15-57.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-15-57.png)
    
    ![Screenshot from 2024-09-06 17-17-30.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-17-30.png)
    
    ![Screenshot from 2024-09-06 17-50-22.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-50-22.png)
    
    ![Screenshot from 2024-09-06 17-50-31.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-50-31.png)
    
    ![Screenshot from 2024-09-06 17-50-43.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-50-43.png)
    

## 키보드 Input 추가

이제 키보드에서 설치한 한글 Input을 사용할 수 있게 추가해준다.

- `Setting`을 열고 `Keyboard`에 들어가서, Input Scources를 추가 (`+`) 해준다.

![Screenshot from 2024-09-06 17-57-19.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-57-19.png)

![Screenshot from 2024-09-06 17-57-45.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-57-45.png)

- 반드시 `Hangul`이라고 적힌 것을 추가해야 한다.

![Screenshot from 2024-09-06 17-58-18.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-58-18.png)

- 이를 추가하고 나면, Input Sources에 Korean(Hangul)이 표시된 것을 볼 수 있다. 또한 오른쪽 상단에 en 표시를 눌러보면, 아래에 Korean (Hangul) 표시가 추가된 것을 볼 수 있다.
    
    ![Screenshot from 2024-09-09 10-04-58.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-09_10-04-58.png)
    
    ![Screenshot from 2024-09-06 17-59-41.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-06_17-59-41.png)
    
- 이때 아래에 추가된 Korean(Hangul)을 눌러보면, 언어 변경 toggle이 나타나며, 이제 `shift + space bar`를 누르면 한영 변환이 가능하다.
    
    ![Screenshot from 2024-09-09 09-59-11.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-09_09-59-11.png)
    

## 한영키 사용

위 처럼 shift + space 바만 사용하는 것 대신 한영 키를 사용하고 싶으면 한글 토글을 추가하면 된다.

- Setting의 Keyboard에 Korean (Hangul)의 오른쪽 점 세 개를 눌러서 preference에 들어가서 `Add`를 누르면 아래와 같은 창이 뜬다. 이때 한영키를 눌러주면 된다.
    
    ![Screenshot from 2024-09-09 10-02-54.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-09_10-02-54.png)
    
    ![Screenshot from 2024-09-09 10-03-26.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-09_10-03-26.png)
    
    ![Screenshot from 2024-09-09 10-04-00.png](../../assets/images/2024-10-12-ubuntu22-korean-keyboard/Screenshot_from_2024-09-09_10-04-00.png)
    

## 안정적 한영 변환 사용

위의 방식처럼 세팅하려 할 때 잘 되지 않거나, 일부 창에서면 잘 작동하는 경우가 많이 있다.

예를 들면 terminal에서는 정상적인 한영 변환이 되지만, chrome 등에서는 되지 않는 것이다. 이를 좀 더 안정적으로 사용하려면 아래 설정을 해 주는 것이 좋다.

- 터미널에서 아래 명령어를 입력한다.

```bash
sudo gedit /usr/share/X11/xkb/keycodes/evdev
```

- 창이 뜨면 내용을 아래와 같이 수정한 후 저장한다.
    - <RALT >  = 108 항목 주석 처리 (앞에 // 추가)
    - <HNGL> = 130 항목을 108로 변경
        - 이때 앨리스 배열 등 일반적인 텐키리스 키보드 배열이 아닌 경우, 해당하는 숫자가 다를 수 있다. 이땐 `xev`를 터미널에 입력 후, 사용하고자 하는 키를 눌러보면 해당 키의 번호를 알 수 있다.
- 위 과정이 끝나면 다시 `Reboot` 한다.

## 참고자료

- [https://osg.kr/archives/913](https://osg.kr/archives/913)
- [https://jongsky.tistory.com/8](https://jongsky.tistory.com/8)