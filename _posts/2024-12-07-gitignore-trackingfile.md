---
title: "[Setting] Tracking 중이던 파일에 .gitignore 적용하기 (git origin에서 삭제)"
categories:
- Setting
tags:
- git
---

우선 `.gitignore` 파일에 더 이상 tracking하지 않고 git에서 삭제하고 싶은 파일이나 폴더들을 추가한다.

이후 터미널에서 아래 명령어들을 차례로 수행하면 된다.

```
git rm -r --cached .
git add .
git commit -am "Remove ignored files"
```

## 참고자료

- [https://cppmaster.tistory.com/entry/Git에-tracking중인-file을-ignore-하는-방법](https://cppmaster.tistory.com/entry/Git%EC%97%90-tracking%EC%A4%91%EC%9D%B8-file%EC%9D%84-ignore-%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95) [연어포케:티스토리]