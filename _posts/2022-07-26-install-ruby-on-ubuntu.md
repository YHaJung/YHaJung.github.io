---
title: "Ubuntu 우분투에 ruby 설치하기"
categories:
  - 사용법
tags:
  - ubuntu
---


## 0. 잘못 설치된 ruby가 이미 있을 경우
가장 일반적으로 ruby를 설치하려고 하면 아래와 같은 명령어를 쓰곤한다.
```
sudo apt update
sudo apt install ruby-full
```
하지만 이렇게 설치할 경우 아래와 같은 permission error가 발생하곤 한다.

[You don't have write permissions for the /var/lib/gems/2.3.0 directory]

먼저 이미 위와 같은 에러가 발생할 경우 ruby를 제거해준다.

```
sudo apt-get remove ruby
```

이제 안전하게 다시 ruby를 설치해 보자.

## 1. ruby 설치에 필요한 패키지 설치
```
sudo apt-get remove ruby
sudo apt update
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev
```

## 2. rbenv와 ruby-build 설치
```
curl -sL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash -
```

## 3.Path 경로에 $HOME/.rbenv/bin 추가 (Bash 사용을 가정)
```
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

## 4. Ruby 설치
```
rbenv install 3.1.2
rbenv global 3.1.2
```
> 안전한 ruby 최신 버전 확인은
`rbenv install -l`를 통해 할 수 있다.

## 5. 설치 결과 확인
```
ruby -v
```

## + rubygems 설치
```
sudo apt-get install rubygems
```

## 참고
- https://stackoverflow.com/questions/37720892/you-dont-have-write-permissions-for-the-var-lib-gems-2-3-0-directory