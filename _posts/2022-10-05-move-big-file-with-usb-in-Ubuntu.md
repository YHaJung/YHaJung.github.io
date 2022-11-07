---
title : "Ubuntu에서 usb로 4.2GB 이상 옮기기"
categories:
    - data
tags:
    - ubuntu
    - data
---

- partition의 형식을 FAT가 아닌 NTFS나 Ext4 등으로 바꿔 주어야 한다.
    - FAT 형식의 최대 용량이 4.2GB이다.

## 바꾸는 방법

- disks 설정으로 들어간다.
    
    ![Untitled](/assets/images/2022-10-05-images/2022-10-05-img01.png)
    
- 원하는 usb 파티션의 설정 버튼을 누른 후 `format partition`을 선택한다.
    
    ![Untitled](/assets/images/2022-10-05-images/2022-10-15-img02.png)
    
- 이후 원하는 것으로 `Type`을 바꿔주면 된다.