---
title: "[Setting] WSL에 네트워크 드라이브 마운트하기"
categories:
- Setting
tags:
- WSL
---

윈도우에서 일반 c 드라이브에서는 네트워크 폴더 연결이 되고 나면, python 코드나 bash 등에서 바로 해당 경로로 접속할 수 있다.

하지만 WSL 환경에서는 네트워크 드라이브에 바로 접근 되지 않는다.

이 글에서는 WSL 환경에서 네트워크 드라이브에 경로 주소로 바로 접근하기 위한 방법을 소개한다.

## 1. 드라이브 마운트

- 먼저 윈도우 환경에서 원하는 네트워크 드라이브를 마운트해 둔다.
- 원하는 네트워크 폴더 `우클릭` - `네트워크 드라이브 연결...` 선택하여 연결한다.

![Untitled](../../assets/images/2024-12-31-wsl-network-drive-mount/Untitled.png)

## 2. WSL에 마운트

```jsx
sudo -S mount -t drvfs Z: /mnt/z/
```

## 3. 자동 마운트

~/.bashrc에 추가해주면 자동 적용된다.

## 참고자료

- [https://cho-et-al.tistory.com/15](https://cho-et-al.tistory.com/15)