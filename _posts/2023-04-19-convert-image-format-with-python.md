---
title : "[python] python으로 image 파일 변환 : png ↔ jpg(jpeg)"
categories:
  - python
tags :
  - python
  - image
---

- PIL 설치

```bash
pip install Pillow
```

- 변환

```bash
from PIL import Image
im = Image.open(원본파일).convert('RGB')
im.save(새로운 파일, 파일형식명)
```

```bash
# 예시 (png -> jpg)
from PIL import Image
im = Image.open('bryan.png').convert('RGB')
im.save('hello.jpg', 'jpeg')
```