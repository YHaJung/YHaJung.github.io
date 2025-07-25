---
title: "[C++] Visual Studio에서 메모리 할당 상태 점검 & 메모리 비우기"
categories:
- Manual
tags:
- C++
- Visual Studio
- cpp
- memory
---

Python의 경우, 사용하지 않는 인스턴스들은 자동으로 삭제된다. (check)

하지만 C++의 경우, 이런 작업이 자동으로 일어나지 않고 프로그래머가 해당 내용을 지시해주어야 한다.

이때 현재 과도하게 사용되거나, 누적되어  계속 생성되고 있는 인스턴스들이 있는지 확인하는 방법을 소개한다.

## 메모리 할당 상태 점검

1. Debug 모드로 실행한다.
2. 진단 도구 확인하기
    1. 일반적인 경우, 자동으로 진단 도구(Diagnostics Tools) 창이 나타난다.
    2. 나타나지 않을 경우, `디버그(Debug)` - `창(Windows)` - `진단 도구 표시(Diagnostics Tools)` 를 선택하거나 `ctrl + alt + F2`를 누르면 나타난다.
3. 나타난 진단 도구에서 `메모리 사용량` 에 들어가서 `스냅샷 만들기` 를 선택한다. 이후 생성된 스냅샷을 선택하고, `힙 보기` 를 누르면, 왼쪽과 같은 창이 나타난다. 이를 통해서 스냅샷을 만든 시점에 할당되어있는 인스턴스들과 해당 인스턴스들이 차지하는 메모리 크기를 확인할 수 있다.
    
    ![image.png](../../assets/images/2024-10-29-cpp-visual-studio-check-memory/image.png)
    
4. 그곳에서 과하게 메모리를 많이 차지하고 있는 것으로 보이는 개체형식을 더블클릭 해보면, 해당 개체 형식의 인스턴스들을 볼 수 있다. (모든 항목이 이 보기에서 필터링되었습니다. 라고 뜨고, 몇 초 기다려야 실제 내용이 뜨는 경우가 있다. 인내심을 가지고 조금은 기다려보자.)
5. 나타난 인스턴스 중 원하는 것을 선택하면, 아래에 해당 인스턴스들이 호출되는 위치들을 확인할 수 있다. 이를 확인해보고, 더 이상 필요 없을 것으로 보이는 위치에서, 해당 인스턴스들을 삭제하도록 코드를 작성하면 된다.
    
    ![image.png](../../assets/images/2024-10-29-cpp-visual-studio-check-memory/image%201.png)
    

## 메모리 비우기

필요없는 메모리가 계속 누적되고 에러가 발생하는 경우, 대부분 동적 메모리가 할당(new) 후 해제(delete) 되지 않아서 반복 생성되고 있는 것이다.

이를 해결하기 위해선 아래 게시글을 참고해서 할당한 메모리를 사용 후엔 모두 비우도록 코드를 작성한다.

- [[C++] new, delete를 통한 동적 메모리 할당 및 비우기](%5BC++%5D%20new,%20delete%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%20%E1%84%86%E1%85%A6%E1%84%86%E1%85%A9%E1%84%85%E1%85%B5%20%E1%84%92%E1%85%A1%E1%86%AF%E1%84%83%E1%85%A1%E1%86%BC%20%E1%84%86%20465a83dc863044d38e436731ab504e05.md)