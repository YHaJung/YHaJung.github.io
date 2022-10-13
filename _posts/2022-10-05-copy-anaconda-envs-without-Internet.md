---
title : "Copy Anaconda Envs without Internet"
categories:
    - 사용법
tags:
    - bash
    - anaconda
---

## Conda pack 설치

기존 위치와 새로 만들 위치 모두에 conda-pack을 설치한다.

```bash
pip install conda-pack
```

## tar.gz 파일로 압축

복사할 파일을 압축한다.

```bash
conda pack -n my_env [-o out_name.tar.gz]
```

- error fix
    
    아래와 같은 에러가 나올 때가 있다.
    
    detectron2와 같이 폴더 형태로 생성되어 수정할 수 있는 기능들이 포함되어 있는 경우 나타나는 에러이다.
    
    ```bash
    CondaPackError: Cannot pack an environment with editable packages
    installed (e.g. from `python setup.py develop` or
     `pip install -e`). Editable packages found:
    ```
    
    해당 파일들은 코드를 따로 압축하여 이동하면되므로, 아래와 같은 옵션을 추가한다.
    
    ```bash
    --ignore-editable-packages
    ```
    

## 압축해제

- usb 등 인터넷과 무관한 하드디스크로 압축파일을 복사해 이동한 후, 압축을 해제한다.

```bash
mkdir -p my_env
tar -xzf my_env.tar.gz -C my_env
```

- 복사한 환경을 활성화한다.

```bash
source my_env/bin/activate
```

- prefix를 청소한다.

```bash
conda-unpack
```

## 참고자료

- [https://www.anaconda.com/blog/moving-conda-environments](https://www.anaconda.com/blog/moving-conda-environments)
- error
    - https://github.com/conda/conda-pack/issues/98
    - [https://www.codestudyblog.com/cs2201py/40102071722.html](https://www.codestudyblog.com/cs2201py/40102071722.html)