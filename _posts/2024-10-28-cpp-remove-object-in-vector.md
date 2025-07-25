---
title: "[C++] vector에서 특정 객체 삭제하기(remove, erase 차이 및 사용법)"
categories:
- C++
tags:
- C++
- erase
- remove
- vector
---

## 요약

```cpp
using namespace std;
#include <algorithm>

// numbers vecotr에서 'b'라는 원소를 삭제하기
numbers.erase(remove(numbers.begin(), numbers.end(), 'b') numbers.end();
```

## 소개

C++에서 기본 자료형인 배열(Array)를 사용할 경우, 동적 크기 할당이 불가능하다.

이런 불편을 해결하기 위해, 동적 크기의 객체인 std의 vector 컨테이너를 많이 사용한다.

그런데 vector 컨테이너는 특정 원소를 찾아서 삭제하려다 보면 생각처럼 작동하지 않는 경우를 자주 만나게  될 것이다.

vector의 2가지 삭제 함수인 remove, erase의 각각 작동과, 안전하게 원하는 원소를 삭제하는 방법을 소개하겠다.

## Remove 함수

```cpp
#include <algorithm>

remove(first_iterator, last_iterator, 삭제하려는 값);
```

- remove 함수를 algorithm 해더를 선언하고 사용해야 한다.
- [first, last) 사이를 탐색하면서, 삭제하려는 값을 모두 찾는다.
- 남은 원소들이 삭제하는 값들만큼 앞으로 당겨진다.
- 이동 후, 남은 원소들 중 마지막 원소의 다음 위치의 iterator를 반환한다.
- 예시
    
    ```cpp
    vector<int> numbers = {1, 2, 3, 2, 2, 4};
    
    vector<int>::iterator iter = remove(numbers.begin(), numbers.end(), 2);
    ```
    
    - numbers에서 2를 빼고 나면 1, 3, 4가 남으므로, 마지막 값인 4의 바로 뒤의 위치를 가리키는 값이 return 된다.
- 문제점!!
    - vector의 size는 줄어들지 않는다!! 앞으로 이동 만하고 뒤 원소들은 그대로 남는다.
    - 예시 :  위 예시에서 remove 후의 numbers는 {1, 3, 4, 2, 2, 4} , size 6이다.

## Erase 함수

```cpp
using namespace std;

numbers.erase(first_iterator, last_iterator);  // [first, last) 모두 삭제
numbers.earse(삭제할원소 iterator 위치);       // 특정 위치 원소 삭제
```

- [first, last) 범위를 모두 삭제하거나, 특정 위치의 원소를 삭제할 수 있다.
- 해당 위치를 삭제 후, 자동으로 size가 줄어든다.
- 마지막으로 삭제한 원소 바로 뒤 원소의 삭제 후 위치를 return한다.
- 예시
    
    ```cpp
    vector<int> numbers = {1, 2, 3, 6, 7, 4};
    
    numbers.erase(idx 1의 위치, idx 3의 위치);
    ```
    
    - numbers에서 {2, 3} 범위를 삭제하게 되므로 numbers = {1, 6, 7, 4}가 되고, size는 4가 된다.
    - 마지막으로 삭제된 3의 다음 값은 6이다. 따라서 삭제 후 6의 위치인 idx 2를 가리키는 iterator가 return 된다.
- 문제점
    - return 값이 무의미하다.
        - 위 예시에서 6의 위치의 iterator를 받아도 딱히 쓸모가 없다.
    - 삭제 위치를 알아내서 적용하기 어렵다.
        - idx도 아니고, 주소도 아닌, iterator 위치이다. 맨 앞 원소 하나(numbers.begin()) 혹은 맨 뒤 원소 하나(numbers.end())를 삭제할 게 아니면 위치를 모른다…

## Remove와 Erase를 합쳐서 사용하기

```cpp
vector<int> numbers = {1, 2, 3, 2, 2, 4};

numbers.erase(remove(numbers.begin(), numbers.end(), 2) numbers.end();
```

위와 같이 사용하면

1. remove가 2들을 만큼 원소들을 앞으로 당긴 후, 남은 원소들의 위치 뒤의 iterator를 반환한다.
    1. numbers = {1, 3, 4, 2, 2, 4} 이고, idx 3의 iterator 위치를 반환한다.
2. erase가 idx 3의 iterator에서 numbers.end()까지를 모두 삭제하고 size를 줄인다.
    1. {2, 2, 4} 범위가 삭제되며 numbers = {1, 3, 4} size는3이 된다.

이를 통해 각자의 단점을 보완해서 사용할 수 있다.

## 참고자료

- [https://velog.io/@cse_pebb/C-remove-함수-vs.-vector의-erase-함수](https://velog.io/@cse_pebb/C-remove-%ED%95%A8%EC%88%98-vs.-vector%EC%9D%98-erase-%ED%95%A8%EC%88%98)