---
title: "깃블로그 만들기"
categories:
  - 사용법
tags:
  - blog
---


## 1. Jekyll 디자인 선택 & 가져오기
아래와 같은 사이트 들에서 마음에 드는 블로그 테마를 선택한다.
- http://jekyllthemes.org/
- https://jekyllthemes.io/free
- http://themes.jekyllrc.org/
- https://github.com/topics/jekyll-theme


원하는 디자인의 github에 들어가 코드를 가져온다.
- 방법 1. fork(코드 복사) 선택한다. 이후 Repository name을 (자신의 ID).github.io로 설정하고 Create Fork 선택한다.
![](https://velog.velcdn.com/images/recoder/post/b2362ff7-6523-4977-8ff7-dc6952688e63/image.png)
![](https://velog.velcdn.com/images/recoder/post/0f2dfe2a-8b79-478e-b449-01fa2c277b3d/image.png)

- (추천) 방법 2. Code를 zip 파일로 다운로드해서 사용한다.
기존 branch, commit들과 분리되고, issue 텝이 생기는 장점이 있다.
우선 (자신의 ID).github.io라는 이름으로 새로운 repository를 만든다.
![](https://velog.velcdn.com/images/recoder/post/f19366bb-971a-42ee-b458-9f71408c4855/image.png)
그리고 원하는 디자인의 github repository에서 모든 코드를 zip으로 다운로드 후 압축해제해서, 방금 만든 repository에 넣는다.
![](https://velog.velcdn.com/images/recoder/post/e6692143-05c6-468a-9ef1-60b77fede091/image.png)

## 2. 블로그 출시하기
_config.yml 파일을 열어, url 항목에서 주석을 지워 "https://(자신의ID).github.io" 구조로 바꾸고 저장한다.
![](https://velog.velcdn.com/images/recoder/post/0ad7cc6f-5dcf-41db-9203-f079783a1bd2/image.png)

인터넷 브라우저를 열고 설정한 url 주소(https://(자신의ID).github.io)로 가보면 페이지가 생성된 것을 확인할 수 있다.
![](https://velog.velcdn.com/images/recoder/post/b332d5f0-ad40-43f4-8160-6e5c2ef80ba0/image.png)
  - 필자와 같은 minimal-mistakes 디자인을 사용한 경우, 생성한 페이지 오른쪽 상단에 뜨는 "Quick-Start Guide"를 참고해 도움을 받을 수 있다.

위 과정을 거치면, 아주 간단히 자신만의 블로그가 생성되었다.
파일 수정은 일반적인 github 사용법과 똑같이 하면 된다.(깃블로그 사용자라면 깃허브 사용에 익술할 것으로 믿는다. 아니라면 velog, notion, tstory 등 다른 블로그를 추천한다.)

## 3. local 사용 세팅
깃블로그를 로켈에서 수정하고, github에 반영하기 전 로컬에서 확인해볼 수 있도록 하는 작업이다.

- Window  
  https://jekyllrb.com/docs/ 를 따라 필요한 프로그램들을 다운로드 한다.
  - ruby 다운로드  
  https://rubyinstaller.org/ 에서 파일 다운로드 및 실행한다.
  ![](https://velog.velcdn.com/images/recoder/post/4c33c9c9-33fa-4ed9-b26c-f12d58c34acb/image.png)
  ![](https://velog.velcdn.com/images/recoder/post/7c9518a8-8715-4210-9f32-d32a0d3b4293/image.png)

  - 기본 설정을 따라서 설치를 진행하면, 아래와 같은 창이 뜬다. 여기에 3을 입력하고 enter를 누른다.  
  ![](https://velog.velcdn.com/images/recoder/post/077e979b-00eb-4160-8f7a-5af6c15ead28/image.png)

  설치가 완료되면 종료한다.(enter 입력시 종료됨)

- Ubuntu
  > 위는 Window에서 ruby를 설치하는 방법이다. 만약 Ubuntu에서 설치를 하고 싶다면 [우분투에 ruby 설치하기](https://yhajung.github.io/%EC%82%AC%EC%9A%A9%EB%B2%95/install-ruby-on-ubuntu/) 를 참고하자.


- jekyll과 bundler 설치 
cmd 혹은 terminal에 아래 명령어를 입력한다.
```
gem install jekyll bundler
bundle install
```

- local server 구동하기
gitblog의 local code 폴더로 이동한 후, 아래 명령어를 입력한다.
```
bundle exec jekyll serve
```
![](https://velog.velcdn.com/images/recoder/post/519b354f-2028-47b5-a330-fdd6b8b1ad4b/image.png)


여기서 나타난 server address를 인터넷 브라우저로 열면, 실제 blog에 반영하기 전에 local에서 변경 결과를 확인할 수 있다.
![](https://velog.velcdn.com/images/recoder/post/50cca9ae-e3ed-4f2e-a44a-c9defa1a1d58/image.png)
이때 에러가 발생하는 경우가 있다.
에러 메시지에서 없다고 하는 기능이 있을 경우 bundle add 명령어로 추가해준다.
![](https://velog.velcdn.com/images/recoder/post/3deacaf6-5cf2-42e9-876f-270f56f261c1/image.png)

필자의 경우 아래와 같은 2가지를 추가하였다.
```
bundle add jekyll-sitemap
bundle add webrick
bundle add wdm
```

이후 다시 "bundle exec jekyll serve"를 입력해보면 성공적으로 server가 구동하는 것을 확인할 수 있다.

## 4. 불필요한 파일 제거
기존 디자인을 clone 해올 경우 불필요한 파일들도 포함되어 있다. 이를 제거해준다.

필자가 사용한 minimal-mistakes의 경우 아래 파일들이 이에 해당한다.
- .editorconfig
- .gitattributes
- .github
- CHANGELOG.md
- screenshot-layouts.png
- screenshot.png

추가로 아래 두 폴더의 경우 삭제해도 무방하다. 하지만 새로운 구조나 게시글을 만들 때 참고하면 좋을 예시이므로 gitblog에 익숙하지 않은 사용자는 남겨두기를 권장한다.
(블로그에 직접적으로 반영되진 않는다.)
- /docs
- /test

또한 README.md 파일의 경우, 블로그 소개를 위한 파일이다. 내용을 모두 삭제하고 원하는 소개 문구를 넣으면, github에서 확인할 수 있다.(파일을 삭제해도 무방하다.)

## 4. 게시글 생성
- _posts 폴더 안에 .md 파일을 생성한다.
- 파일명은 yyyy-mm-dd-title 구조로 한다.
  - title은 post의 url에 반영된다.
  - /test/_posts 혹은 docs/_posts 속에 있는 md 파일을 가져와서 빠르게 테스트 해볼 수 있다.

- 파일 맨 앞에 아래와 같은 구조로 제목, 카테고리, 테그 등을 지정할 수 있다.(생략 가능)

```
---
title: "Edge Case: Nested and Mixed Lists"
categories:
  - Edge Case
tags:
  - content
  - css
  - edge case
  - lists
  - markup
last_modified_at: 2016-03-09T16:20:02-05:00
---
```

## 5. 페이지 구조 수정
### navigation
_data/navigation.yml 파일을 수정한다.
  - url은 상대경로, 절대경로 모두 사용 가능하다.
  - 상대경로의 경우, _pages 폴더 속 md 파일의 permalink 항목과 연결된다.
    - _pages 폴더는 직접 생성한다.
    -  .md 파일은 docs/_pages 속 파일들을 복사해서 생성한다.

<_data/navigation.yml 예>
```
main: # url엔 상대경로와 절대경로 모두 가능
  - title: "Category"
    url: /categories/
  - title : "Tag"
    url : /tags/
  - title: "Year Archive"
    url: /year-archive/
 ```

### Home page 정보 수정
_config.yml을 수정한다.
- 해당 파일의 수정사항들을 local에서 확인하고 싶을 경우 새로 로드(bundle exec jekyll serve를 다시시행) 해야 확인할 수 있다.

대표적으로 수정해야할 부분들은 아래와 같다.
![](https://velog.velcdn.com/images/recoder/post/1a8c1d50-28f9-425c-a99c-323097160b02/image.png)


```
minimal_mistakes_skin    : "default" ## 테마색


# A 파트
# Site Settings
locale                   : "ko-KR"   # 언어지정. 국가별 언어 코드
title                    : "Blog Name"  # 블로그 이름
title_separator          : "-"
subtitle                 : "블로그 소개글" 블로그 소개글

# B 파트
name                     : "이름"   # 하단 작성자

# E 파트
 atom_feed:
  path                   : # blank (default) uses feed.xml
  hide                   : true # true, false (default)
  
# C 파트
author:
  name             : "작성자"
  avatar           : # path of avatar image, e.g. "/assets/images/bio-photo.jpg"
  bio              : "I am an **amazing** person."
  location         : "Somewhere"
  email            :
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope-square"
      url: "mailto:hajung3768@gmail.com"
    - label: "Website"
      icon: "fas fa-fw fa-link"
      url: "https://your-website.com"
 
# D 파트
# Site Footer
footer:
  links:
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: #"https://github.com/깃아이디"
      

```

## 참고
- https://honbabzone.com/jekyll/start-gitHubBlog/
- https://www.youtube.com/watch?v=ACzFIAOsfpM