---
title: "CVAT을 통한 무료 Annotation"
categories:
  - 사용법
tags:
  - data
  - Annotation
---

Computer Vision을 위한 무료 Annotation Tools에는 CVAT, LabelMe, Labeling, VoTT 등이 있다.

이 중 CVAT 사용법을 알아보자.

## CVAT(Computer Vision Annotation Tool)이란?

- Web based Annotation Tool
    - 사이트 주소 : [https://app.cvat.ai](https://app.cvat.ai/auth/login)
- the primary tasks of supervised machine learning의 primary task들에 labelling
    
    : image classification, object detection, image segmentation 등
    
- four basic types of annotation: boxes, polygons, polylines, and points

## 사용법

- [사이트](https://app.cvat.ai/)에 들어가 회원가입 후 로그인한다.
    
    ![Untitled](/_posts/2022-11-07-images/Untitled.png)
    
- `project` 텝으로 들어가서 `Create a new project`를 선택한다.

    ![Untitled](/_posts/2022-11-07-images/Untitled%201.png)

- `Project이름을 설정`하고, `Constructor`에서 원하는 `label을 추가`하고, `Submit & Open`을 선택한다.
    
    ![Untitled](/_posts/2022-11-07-images/Untitled%202.png)
    
    ![Untitled](/_posts/2022-11-07-images/Untitled%203.png)
    
    - Setup skeleton은 무시하면 된다.
- 오른쪽 아래 + 버튼을 눌러 `Create a new task`를 선택한다.
    
    ![Untitled](/_posts/2022-11-07-images/Untitled%204.png)
    
- task이름을 설정하고, 이미지를 선택 후 submit & open을 누르면 서버에 이미지가 업로드 된다.
    - 시간이 꽤 걸리므로 기다린다.
        
    ![Untitled](/_posts/2022-11-07-images/Untitled%205.png)    
    ![Untitled](/_posts/2022-11-07-images/Untitled%206.png)
    
- 생성한 job으로 들어가서 labelling을 시작한다.
    ![Untitled](/_posts/2022-11-07-images/Untitled%207.png)
    
- 다 끝났다면 projects 탭으로 들어가서, `Export Dataset`을 선택한다.