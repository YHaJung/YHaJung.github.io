---
title: "[Setting] GPU 사용을 위한 컴퓨터 기본 세팅 (ver. Ubuntu)"
categories:
- Setting
---

- [Anaconda 다운로드 페이지](https://www.anaconda.com/products/distribution#linux)에 가서 컴퓨터 환경과 python 버전에 맞는 anaconda를 다운로드 한다.
- bash 명령어로 다운로드한 파일을 설치한다.(파일은 Download 폴더에서 확인할 수 있다.)

```bash
bash Anaconda3-2022.05-Linux-x86_64.sh
```

- space 혹은 enter 키를 누르며 넘기다가 'Do you accept the license terms? [yes/no]' 라는 질문이 나오면 yes를 선택한다.
- [/home/(username)/anaconda3] >>> 가 나오면 enter를 누른다.
- PATH 에 아나콘다를 넣을지 물어보는 문구가 나오면 yes 를 선택한다.
    - 만약 뜨지 않을 시에는 종료 후 직접 추가한다.
        
        ## **1. Anaconda 설치 및 세팅**
        
        ```bash
        echo 'export PATH="/HOME/[username]/anaconda3/bin:$PATH"' >> ~/.bashrc
        
        source ~/.bashrc
        ```
        

### **가상환경 만들기**

```bash
# 기존 가상환경 종류 확인
conda info --envs

# 가상환경 만들기
conda create -n [가상환경이름] python=3.7

# 가상환경 활성화
conda activate [가상환경이름]

# 가상환경 비활성화
conda deactivate
```

## **2. Nvidia Driver 설치**

- 추천 버전 확인

```bash
ubuntu-drivers devices
```

- Software Updater -> settings -> Additional Driver -> 추천 버전 선택 -> Apply Change -> restart

![Untitled](../../assets/images/2024-11-24-gpu-setting/Untitled.png)

![image](../../assets/images/2024-11-24-gpu-setting//user-images.githubusercontent.com/49065638/180959110-93690155-cc34-43e9-8976-f8bc03c5c9f5.png](https://user-images.githubusercontent.com/49065638/180959110-93690155-cc34-43e9-8976-f8bc03c5c9f5.png))

![image](../../assets/images/2024-11-24-gpu-setting//user-images.githubusercontent.com/49065638/180959781-b3c9112b-37f7-44f3-be58-e8b4b07c22ab.png)

![Untitled](../../assets/images/2024-11-24-gpu-setting/Untitled%201.png)

- 설치 확인 및 CUDA 버전 확인

```bash
nvidia-smi
```

![Untitled](../../assets/images/2024-11-24-gpu-setting/Untitled%202.png)

## **3. CUDA toolkit 설치**

- 앞서 확인한 CUDA 버전에 맞는 [cuda toolkit](https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=16.04&target_type=runfile_local)을 설치한다. 위에서 확인한 숫자보다 낮은 버전을 설치할 수 있다.

![Untitled](../../assets/images/2024-11-24-gpu-setting/Untitled%203.png)

```bash
$ wget https://developer.download.nvidia.com/compute/cuda/11.3.0/local_installers/cuda_11.3.0_465.19.01_linux.run

$ sudo sh cuda_11.3.0_465.19.01_linux.run
```

- 환경변수 경로 설정

```bash
vim ~/.bashrc

# 파일 맨 밑에 추가
export CUDA_HOME=/usr/local/cuda-11.3
export PATH=/usr/local/cuda-11.3/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.3/lib64:$LD_LIBRARY_PATH

source ~/.bashrc
```

- 설치확인

```bash
nvcc -V
```

![Untitled](../../assets/images/2024-11-24-gpu-setting/Untitled%204.png)

## 4. CuDNN 설치

- [https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive) 에서 버전에 맞는 파일 다운로드

![Untitled](../../assets/images/2024-11-24-gpu-setting/Untitled%205.png)

```bash
tar xvzf cudnn-11.3-linux-x64-v8.2.1.32.tgz

sudo cp cuda/include/cudnn* /usr/local/cuda-11.3/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-11.3/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda-11.3/lib64/libcudnn*

# or
# tar -xvf *.tar.zx
# cd (folername)
# sudo cp ./include/cudnn* /usr/local/cuda-11.1/include
# sudo cp ./lib/libcudnn* /usr/local/cuda-11.1/lib64
# sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda-11.1/lib64/libcudnn*

```

- 아래 명령어로 제대로 설치 되었는지 확인한다.

```bash
cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
```

재대로 설치되었을 경우 "#define CUDNN_MAJOR 8"을 확인하실 수 있다.

## 5. Pytorch 설치

- anaconda 환경을 활성화한다.

```bash
conda activate 환경이름
```

- [pytorch 홈페이지](https://pytorch.org/get-started/locally/)로 가서 원하는 버전대로 설치한다.

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.3 -c pytorch -c nvidia
```

## **참고**

- https://shrouded-pamphlet-ced.notion.site/PC-setting-5c1b680f24834d11933beeb81255c50f
- https://velog.io/@hailee98/Ubuntu-CUDA-cuDNN-%EC%84%A4%EC%B9%98
- (윤지) [https://shrouded-pamphlet-ced.notion.site/PC-setting-5c1b680f24834d11933beeb81255c50f](https://www.notion.so/5c1b680f24834d11933beeb81255c50f?pvs=21)
- https://nirsa.tistory.com/332 [Nirsa:티스토리]