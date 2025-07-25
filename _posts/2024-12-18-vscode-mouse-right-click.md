---
title: "[Setting] VSCode 마우스 우클릭으로 실행 - open with code 만들기"
categories:
- Setting
tags:
- VSCode
---

VSCode를 설치할 때, 마우스 우클릭 시 `Open with Code` 버튼이 뜨게 옵션을 선택할 수 있다.

이 옵션을 선택할 시, 특정 폴더에서 마우스 우클릭을 하여 바로 해당 폴더를 VSCode로 열 수 있다.

하지만 설치 당시 해당 옵션을 선택하지 않았을 경우 별도 레지스토리를 추가해주어야 해당 기능을 사용할 수 있다.

## 1. 자동 설치

[open_with_code.reg](%5BSetting%5D%20VSCode%20%E1%84%86%E1%85%A1%E1%84%8B%E1%85%AE%E1%84%89%E1%85%B3%20%E1%84%8B%E1%85%AE%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%B5%E1%86%A8%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%92%E1%85%A2%E1%86%BC%20-%20open%20c72a11e2a76c481fb3c849d542565c0f/open_with_code.reg)

위 파일을 다운하여 실행하면 된다.

## 2. 수동 설치

설치 파일을 온라인으로 받는 것이 찝찝하면 아래와 같이 수동으로 기능을 추가할 수 있다.

### 1) 텍스트 파일 생성

- 아래 내용을 복붙하여 텍스트 파일을 생성한다.

```bash
Windows Registry Editor Version 5.00
; Open files
[HKEY_CLASSES_ROOT\*\shell\Open with VS Code]
@="Edit with VS Code"
"Icon"="C:\\Users\\사용자\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe,0"
[HKEY_CLASSES_ROOT\*\shell\Open with VS Code\command]
@="\"C:\\Users\\사용자\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" \"%1\""
; This will make it appear when you right click ON a folder
; The "Icon" line can be removed if you don't want the icon to appear
[HKEY_CLASSES_ROOT\Directory\shell\vscode]
@="Open with VS Code"
"Icon"="\"C:\\Users\\사용자\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe,0"
[HKEY_CLASSES_ROOT\Directory\shell\vscode\command]
@="\"C:\\Users\\사용자\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" \"%1\""
; This will make it appear when you right click INSIDE a folder
; The "Icon" line can be removed if you don't want the icon to appear
[HKEY_CLASSES_ROOT\Directory\Background\shell\vscode]
@="Open with VS Code"
"Icon"="C:\\Users\\사용자\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe,0"
[HKEY_CLASSES_ROOT\Directory\Background\shell\vscode\command]
@="\"C:\\Users\\사용자\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe\" \"%V\""
```

### 2) 경로 설정

- 위 파일에서 `사용자` 부분을 각자 노트북의 username으로 바꾸어 준다.

- 만약 VSCode를 설치할 때 자동 설정되는 경로 아니라 따로 위치를 설정해 주었다면 아래 작업을 수행하여야 한다.
    - VS Code exe 파일의 경로를 확인한다.
    - 확인한 경로를 위 내용 중 아래 부분 대신 넣는다.
        
        ```bash
        C:\Users\사용자\AppData\Local\Programs\Microsoft VS Code\Code.exe
        ```
        

### 3) 레지스토리에 추가

- `window` + `R` 을 눌러서 `regedit`을 입력한다.
    
    ![Untitled](../../assets/images/2024-12-18-vscode-mouse-right-click/Untitled.png)
    
- 파일 - 가져오기 를 눌러서 생성한 txt 파일을 가져온다.
    
    ![Untitled](../../assets/images/2024-12-18-vscode-mouse-right-click/Untitled%201.png)
    
    - 이때 파일 확장자를 reg에서 모든 파일 혹은 .으로 바꾸어 주어야 txt을 불러올 수 있다.
        
        ![Untitled](../../assets/images/2024-12-18-vscode-mouse-right-click/Untitled%202.png)
        

### (옵션) 자동 설정 파일 만들기

레지스토리 편집기에서, 앞서 생성한 레지스트리 폴더를 `우클리` - `내보내기` 하면 reg 파일을 만들 수 있다.

이후엔 해당 파일을 누르는 것만으로도 동일한 설정을 할 수 있다.

## 참고자료

- [https://esaek.tistory.com/entry/VS-Code-우클릭-시-Open-with-code가-보이지-않을-때](https://esaek.tistory.com/entry/VS-Code-%EC%9A%B0%ED%81%B4%EB%A6%AD-%EC%8B%9C-Open-with-code%EA%B0%80-%EB%B3%B4%EC%9D%B4%EC%A7%80-%EC%95%8A%EC%9D%84-%EB%95%8C)