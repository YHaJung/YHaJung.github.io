---
title: "[Setting] GPU 사용을 위한 컴퓨터 기본 세팅 (WSL ver.)"
categories:
- Setting
tags:
- GPU
- Linux
- WSL
- Windows
---

이 게시글은 WSL2 환경에서 인공지능 학습 용 GPU 사용을 위한 기본적인 세팅들을 설명한다. 이 글은 WSL2 가 이미 설치되어 있다는 것을 가정하고 진행된다. 아직 WSL을 설치하지 않은 경우 WSL 설치 게시글을 참고하길 바란다.

## 1. Nvidia Drive 설치

- wsl에서 gpu를 사용하려면, 먼저 Window에 nvidia driver가 설치되어 있어야 한다.
- Windows에서 Nvidia Driver는 어플리케이션의 형태로 설치 및 확인이 가능하다. 앱을 실행해보고, 아직 설치되어있지 않을 경우 설치를 진행한다. 별도 설정하지 않으면 해당 기종에 맞춰서 추천하는 최신 버전이 설치된다.
- 해당 어플이 없다면, 추후 nvidia toolkit을 설치할 때 드라이버까지 같이 설치할 수도 있으므로 넘어가도 된다.

![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled.png)

![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%201.png)

## 2. gcc 설치

개발 환경에서 많이 사용되기도 하지만, 이후 진행될 cuda toolkit, PyTorch 등 설치에도 gcc가 필요한 경우가 많다. 따라서 우선 gcc를 먼저 설치하고 마저 진행해주는 것이 좋다.

wsl terminal에서 아래 명령을 수행한다. 

```bash
sudo apt update && sudo apt upgrade
sudo apt install gcc
gcc --version # 설치 확인

sudo apt update
sudo apt install build-essential
```

## 3. Cuda Toolkit 설치

- 설치 가능한 버전 확인
    
    Cuda Toolkit의 경우 드라이버에 따라 설치 가능한 버전이 다르다. 아래 키워드를 입력했을 때 확인 가능한 CUDA Version **이하**의 버전들은 사용 가능하다. 만약 사용하고 싶은 CUDA Version이 해당 버전보다 높을 경우, 드라이버를 더 높은 버전으로 새로 설치해 주어야 한다.
    
    ```bash
    nvidia-smi
    ```
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%202.png)
    
- cuda toolkit + 원하는 버전을 검색해서, 환경에 맞춰 선택 후 설치한다.
    
    나는 [cuda 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=runfile_local)을 설치하였다. pytorch 최신 버전들과 잘 호환되는 편이며, Windows 10, 11 용 버전도 존재하며, Ubuntu 18, 20, 22 용 버전도 존재하여 범용적으로 쓰기 편리하기 때문이다.
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%203.png)
    
    ```bash
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
    sudo sh cuda_11.8.0_520.61.05_linux.run
    ```
    
- 안내에 따라 설치를 진행한다.  설치를 원하는 것들만 check하고 `Install`을 누르면 설치가 진행된다. 만약 Nvidia Driver를 아직 설치하지 않았다면 해당 옵션에 check 한다.(cuda toolkit 11.8의 경우, option을 선택하면 driver 설치를 선택할 수 있다.)
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%204.png)
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%205.png)
    
- 경로 설정
    
    설치가 끝나면 나오는 안내문을 참고하여, path 경로를 설정한다. (만약 안내문이 나오지 않는다면, 아래 명령어에서 cuda 버전에 따라 숫자만 바꾸면 된다.)
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%206.png)
    
    ```bash
    vim ~/.bashrc
    
    # 파일 맨 밑에 주석 내용 추가
    # export CUDA_HOME=/usr/local/cuda-11.8/
    # export PATH=/usr/local/cuda-11.8/bin:$PATH
    # export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH
    
    source ~/.bashrc
    ```
    
- 설치 확인
    
    ```bash
    nvcc -V
    ```
    

## 4. Cudnn 설치

- [https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive) 에서 cuda 버전에 맞는 Linux용 tar 파일을 다운로드한다.
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%207.png)
    
- 

```bash
tar -xvf cudnn-linux-x86_64-8.9.3.28_cuda11-archive.tar.zx # 다운한 파일 압축해제
cd (folername)
# 압축해제한 파일들 cuda toolkit에 등록 
sudo cp ./include/cudnn* /usr/local/cuda-11.8/include
sudo cp ./lib/libcudnn* /usr/local/cuda-11.8/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda-11.8/lib64/libcudnn*

# or

# tar xvzf cudnn-11.3-linux-x64-v8.2.1.32.tgz

# sudo cp cuda/include/cudnn* /usr/local/cuda-11.3/include
# sudo cp cuda/lib64/libcudnn* /usr/local/cuda-11.3/lib64
# sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda-11.3/lib64/libcudnn*

```

- 아래 명령어로 제대로 설치 되었는지 확인한다.
    
    재대로 설치되었을 경우 "#define CUDNN_MAJOR 8"을 확인할 수 있다.
    

```bash
cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2

```

## 5. Anaconda 설치

- [Anaconda 다운로드 페이지](https://www.anaconda.com/products/distribution#linux)에 가서 컴퓨터 환경과 python 버전에 맞는 anaconda를 다운로드 한다. 이때 주의할 것은 WSL 사용 환경의 경우, 노트북은 window 이므로 추천해주는 download 버튼을 바로 누르면 window 용이 다운로드된다. 따라서 반드시 **linux installer를 따로 눌러 주어야 한다.**
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%208.png)
    
- bash 명령어로 다운로드한 파일을 설치한다.(파일은 Download 폴더에서 확인할 수 있다.)
    
    ```bash
    bash Anaconda3-2024.02-1-Linux-x86_64.sh
    ```
    
    - 설명에 따라 설치를 진행한다. 대부분 enter 혹은 yes를 입력하면 된다.
        - space 혹은 enter 키를 누르며 넘기다가 'Do you accept the license terms? [yes/no]' 라는 질문이 나오면 yes를 선택한다.
        - [/home/(username)/anaconda3] >>> 가 나오면 enter를 누른다. 이때 해당 경로가 **anaconda 설치 경로**이다. 다른 위치에 설치하고 싶을 경우 해당 경로를 적어주면 된다.
        - PATH 에 아나콘다를 넣을지 물어보는 문구가 나오면 yes 를 선택한다.
            - 만약 뜨지 않을 시에는 종료 후 직접 추가한다. path 경로에 Anaconda 설치 경로를 추가해주면 된다.
                
                ```bash
                vim ~/.bashrc
                
                # 아래 주석 문구를 파일 맨 아래에 추가
                # export PATH=/home/(username)/anaconda3/bin:$PATH
                
                source ~/.bashrc
                ```
                
- Anaconda 활성화
    
    아래 명령어를 입력 후, 터미널을 껐다 켜면, anaconda가 활성화된 것을 확인할 수 있다.
    
    ```bash
    conda init
    ```
    
    ![Untitled](../../assets/images/2024-11-30-gpu-setting-wsl/Untitled%209.png)