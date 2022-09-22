---
title: "wget으로 구글 드라이브에서 파일 불러오기"
categories:
  - 서버
tags:
  - data
  - bash
---


```bash
wget --load-cookies ~/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ~/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id={FILEID}' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id={FILEID}" -O {FILENAME} && rm -rf ~/cookies.txt
```

위 명령에서{FILEID}과 {FILENAME}를 설정해주면 된다.

- FILEID는 두 부분임에 주의하자.

## FILENAME 설정

- 말 그대로 다운로드할 파일의 이름이다.
    - 예시 : datasets.zip

## FILEID 찾기

- 원하는 파일에서 오른쪽 마우스를 눌러서 `공유 가능한 링크 가져오기`, `링크생성` 등을 선택한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51d49431-32ea-48f3-93ec-50585a1c024a/Untitled.png)
    
- 링크복사를 선택한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93005258-50f1-4612-87e1-87a6edd42632/Untitled.png)
    
- 복사된 링크 중 `~~~/d/{아이디}/view~~` 구조의 {아이디}부분이 FILEID이다.