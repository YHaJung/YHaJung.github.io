---
title: "[Setting] Docker에서 GPU 사용 설정하기(with Nvidia Driver)"
categories:
- Setting
tags:
- AI
- Debug
- Deep Learning
- PyTorch
- docker
---

보통 인공지능 학습을 위해 GPU를 사용할 수 있게 세팅하는 것은 굉장히 번거로운 작업을 걸쳐야 한다. cuda toolkit, cudnn, pytorch / tensorflow, anaconda 등 여러 가지를 서로 호환되게 버전을 잘 맞춰서 다운로드 및 설정해야 하기 때문이다. 또한 이 버전들은 모두 각각 사용 중인 OS와도 호환되어야 한다.

하지만 Docker를 사용하는 유저들은 이런 번거로운 과정을 거치지 않아도 된다.

이미 원하는 버전의 ubuntu, cuda toolkit, cudnn, pytorch 등이 모두 설정된 image를 가져와서 시작하면 되기 때문이다.

이 글에선 이를 위한 간단한 설정 방법과 관련된 이미지를 찾기 좋은 방법을 소개한다.

## 필요한 이미지 찾기

먼저 [docker hub](https://hub.docker.com/)에서 원하는 테그를 찾는다.

위 페이지엔 너무 많은 이미지들이 있는 관계로 자주 사용되는 이미지 테크 찾는 방법을 하나 소개해겠다.

인공지능 연구자들은 PyTorch를 활용해 학습을 하는 경우가 많다.

따라서 이 경우를 예시로 쉽게 세팅된 테그를 찾는 법을 소개하겠다.

아래 단계를 따라하면 쉽게  cuda toolkit, cudnn, pytorch, anaconda 등을 한 번에 세팅하기 위한 이미지 테그를 찾을 수 있다.

1. [nvidia의 pytroch release note](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/index.html) 에 들어가서 원하는 조건을 찾는다.
2. [pytorch tag 페이지](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch/tags)에서 해당 release에 대한 tag를 찾는다.
3. 아래 명령어를 수행한다.
    
    ```bash
    docker pull 이미지테그
    ```
    

## Nvidia Driver 설치

Docker에서 GPU를 사용하기 위해선 다른 요소들은 모두 이미지로 한 번에 다운로드 가능하지만, nvidia-driver는 따로 설치해주어야 한다.

사용할 docker image에서 요구하는 사향을 잘 확인하고, 이보다 높은 버전을 설치해야 한다.

먼저 Software & Updates 의 Additional Drivers에 들어간다.

특별히 요구되는 사향이 없다면, 추천하는 버전으로 설치하면 된다.

원하는 버전을 선택하여, `Apply Chages` 를 누르면 설치가 진행된다.

- 설치가 끝나면 재시작해준다.

- 설치 확인

```bash
nvidia-smi
```

## NVIDIA Container Toolkit 설치

- docker에서 NVIDIA cuda toolkit을 활용하여 gpu를 사용하고 싶을 경우, 아래와 같이  `NVIDIA Container Toolkit` 을 설치하고 `configuration` 설정을 해 주어야 한다.
- 이는 gpu option을 사용할 경우 발생할 수 있는 `Error response from daemon: Cannot restart container bc9d05ca2ffe: could not select device driver "" with capabilities: [[gpu]]` 라는 에러의 해결책이기도 하다.
- 아래의 curl 내용은 시기에 따라 변화할 수 있다. 잘 작동하지 않을 시, [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) 를 참조하길 바란다.
    
    ```bash
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
        sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
        sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    ```
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y nvidia-container-toolkit
    sudo systemctl restart docker
    ```
    

## onnxruntime 설치

- `No supported GPU(s) detected to run this container`로 시작하는 에러가 뜰 경우 `onnxruntime`을 설치한다.
    
    ```bash
    pip install onnxruntime
    # 또는 pip install onnxruntime-gpu
    ```
    

## 참고자료

- https://bluecolorsky.tistory.com/110
- [https://stackoverflow.com/questions/75599261/unable-to-use-gpu-in-custom-docker-container-built-on-top-of-nvidia-cuda-image-d](https://stackoverflow.com/questions/75599261/unable-to-use-gpu-in-custom-docker-container-built-on-top-of-nvidia-cuda-image-d)