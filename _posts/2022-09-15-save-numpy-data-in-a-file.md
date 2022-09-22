---
title : "numpy 데이터를 외부파일로 저장하기(save)"
categories :
    - python
tags : 
    - python
    - numpy
---

## 바이너리 파일로 저장하기/불러오기

```python
import numpy as np
x = np.array([0, 1, 2, 3])

# 저장하기
np.save('경로/파일명', x)

# 불러오기
x_loaded = np.load('경로/파일명.npy')
```

## Dictonary 저장/불러오기

파일이 일반 배열이 아닌 dict 형태일 경우, 불러올 때  `allow_pickle=True` 옵션을 추가한다.

```python
result = np.load('경로/파일명.npy', allow_pickle=True)
```

또한 dictionary 형식으로 바꾸기 위해 아래 **3가지 코트 중 하나**를 사용한다.

```python
result.all()
result.any()
result.flat[0]
```

## 참고자료

- [https://rfriend.tistory.com/358](https://rfriend.tistory.com/358)