--- 
title : "[Debug] pyqt error : qt.qpa.plugin: could not load the qt platform plugin \"xcb\" in \"\" even though it was found."
categories:
- Debug
tags:
- debug
- pyqt
---

```bash
pip install pyqt5
```

위와 같은 명령어로 pyqt를 설치할 경우, 아래와 같은 에러가 나오는 경우가 많다.

“qt.qpa.plugin: could not load the qt platform plugin "xcb" in "" even though it was found.”

이 경우 아래 명령어를 추가로 입력해준다.

```bash
sudo apt install python3-pyqt5
```