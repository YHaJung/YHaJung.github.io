---
title : "[C++] Dynamic Memory Allocation in C++ (malloc, new)"
categories:
- c++
tags:
- c++
---

## Dynamic Memory Allocation이란?

- compile time이 아닌 **run time에 메모리 할당**
- **크기 유동적으로 변경**
- 사용 예시 : user input에 따른 메모리 할당, linked list
- 장단점 : Array vs Linked List
    
    
    |  | Array  | Linked List |
    | --- | --- | --- |
    | 특징 | [Static Memory allocation] <br> - compile time에 메모리 할당 <br> - stack에 저장 | [Dynamic Memory allocation] <br> - run time에 메모리 할당 <br> - heap에 저장 |
    | 장점  | - 빠름 <br> - 자동 alloc/dealloc <br> - fragment없이 연속된 저장 | - 유동적인 크기 <br> - 유동적으로 데이터 넣고 빼기 쉬움 |
    | 단점 | 정확한 크기 예측 힘듦 → 메모리 낭비 발생 | - next/prev pointer를 저장할 추가 메모리 필요 <br> - 느림 <br> - 수동 alloc/dealloc <br> - 연속된 변수 중 중간 것부터 dealloc하여 fragment 발생 가능 |

## C에서의 사용법 : **malloc function**

- C++에서도 가능
- #include <stdlib.h>
- allocation
    - parameter : memory size(bytes)
    - return : 할당한 공간을 가리키는 void **pointer** 혹은 **NULL**(메모리 부족. 할당 실패)
- deallocation
    - free function
    - parameter : allocation 시 return 된 pointer

## C++ 버전 : new/new[]

```cpp
int* foo1;
int* foo5;

foo1 = new int;    //int 1개 공간 할당, 시작 부분 가리키는 pointer 반환
foo5 = new int [5];//int 5개 공간 할당, 시작 부분 가리키는 pointer 반환

delete foo1;
delete[] foo5;    //[]안에 숫자 넣을 필요 없다. foo5안에 크기 정보가 들어있기 때문.
```

- foo5를 malloc으로 구현하면
    
    ```cpp
    foo = (int*) malloc(sizeof(int) * 5 + 4);
    ```
    
    이때 추가 할당 된 4 byte가 사이즈에 대한 정보(5)를 저장한다.
    

## new의 **예외 처리(Exceptions)**  : 할당 실패 시

- 기본 : **bad_alloc**
    - 프로그램 running 중 문제 발생 시 발생, 자동으로 프로그램 멈춰 줌.
- 직접 지정 : **nothrow**
    - C style exception
    - 메모리 할당 실패 시, nullptr을 return한다.
    
    ```cpp
    int * foo;
    foo = new (nothrow) int [5];
    if (foo == nullptr) {
    		…
    }
    ```
    

## Class 동적 할당

- new/delete 사용
    - malloc의 경우 공간만 할당해주는 함수이므로, 이와 같이 생성자와 파괴자를 부르는 역할을 할 수 없고 type을 지정할 수 없다. 따라서 malloc으로는 class를 동적 할당하지 못하고, new/delete를 사용하여야 한다.
- new로 class 할당 시, 해당 class의 constructor가 불러진다.
- delete/delete[]로 dealloc 시, []개의 destructor 불러야 한다.

```cpp
Triangle *t2;
t2 = new Triangle(2.0, 2.0, 3.0); //dynamic 선언
```