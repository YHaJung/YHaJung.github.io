--- 
title : "[python] 배열이 기본 전역변수처럼 동작하는 이유 & 배열 복사(copy)와 2차원 배열 복사(deepcopy)"
categories:
- Python
tags:
- python
---


## 문제점

- python 기존 배열은 유지하고 새로운 배열만 수정하고 싶을 경우, 기대했던 것처럼 작동하지 않을 수 있다.

- python에서 배열 일반 변수처럼 복사할 경우, 하나의 원소를 변경하면 **다른 하나의 원소도 같이 변경**되는 문제가 발생한다.
    
    ```python
    list1 = [1,2,3,4]
    list2 = list1
    
    list2[0] = -1
    
    print(list1)   # [-1, 2, 3, 4]
    print(list2)   # [-1, 2, 3, 4]
    ```
    

- 함수 내부에서 배열을 수정할 경우에, 지역 변수로 취급되지 않고 **전역 변수처럼 작동**한다.
    
    ```python
    def fix(list):
        list[0] = -1
        return list
    
    list1 = [1,2,3,4]
    list2 = fix(list1)
    
    print(list1)   # [-1, 2, 3, 4]
    print(list2)   # [-1, 2, 3, 4]
    ```
    

## 원인

- 배열의 경우, 내부적으로 저장될 땐 값을 저장한 **주소를 가진다**. 이로 인해 배열을 그냥 대입해서 복사하면, 새로운 배열도 동일한 주소를 가지게 된다.

![Untitled](../../assets/images/2023-09-20-python-deepcopy/Untitled.png)

- 이로 인해 한 배열의 원소를 수정하면, 다른 배열의 원소도 바뀌는 것이다.

## 해결방법

- `copy()` 함수를 사용하면, 동일한 원소를 가진 새로운 주소의 배열을 생성하여 할당하게 된다.
    
    ```python
    list1 = [1,2,3,4]
    list2 = list1.copy()
    
    list2[0] = -1
    
    print(list1)  # [1, 2, 3, 4]
    print(list2)  # [-1, 2, 3, 4]
    ```
    
    ```python
    def fix(list):
        list[0] = -1
        return list
    
    list1 = [1,2,3,4]
    list2 = fix(list1.copy())
    
    print(list1)  # [1, 2, 3, 4]
    print(list2)  # [-1, 2, 3, 4]
    ```
    

- 만약 **2차원 배열**일 경우, copy()를 사용해도 내부 원소가 함께 변하게 된다.
    
    ```python
    list1 = [[1,2,3], [4, 5, 6]]
    list2 = list1.copy()
    
    list2[0][0] = -1
    
    print(list1)    # [[-1, 2, 3], [4, 5, 6]]
    print(list2)    # [[-1, 2, 3], [4, 5, 6]]
    ```
    
- 이는 배열의 원소가 주소가 되어, 해당 주소 속을 수정하게 되기 때문이다. 이 경우엔 **copy** 모듈의 `deepcopy()`를 사용하여야한다.
    
    ```python
    import copy
    
    list1 = [[1,2,3], [4, 5, 6]]
    list2 = copy.deepcopy(list1)
    
    list2[0][0] = -1
    
    print(list1)    # [[1, 2, 3], [4, 5, 6]]
    print(list2)    # [[-1, 2, 3], [4, 5, 6]]
    ```