---
title : "[C++] Advanced Function : function관련 유용한 기능들"
categories:
- c++
tags:
- c++
---

## Advanced Call-by-Reference

- function parameter에 & 표시를 붙이면, 포인터를 일반 변수처럼 쓸 수 있다.
- 실제로는 들어온 parameter의 주소를 불러와 사용하지만, 내부에선 일반 변수처럼 작동한다.

```cpp
void swap(int &x, int&y){
	int temp = x;
	x = y;
	y = temp;
}

int intA = 10, intB = 20;
swap(intA, intB)
```

- const references
    - 주소를 불러오지만 변경을 못함 (변경 시도하면 compile error 발생)
    - **read-only**일 때 사용
    - 장점 : call-by-value 장점인 원본 유지의 안정성 + call-by-reference 장점인 추가 메모지 사용 안함.
    
    ```cpp
    void swap(const int &x, const int &y){
    }
    ```
    

## Default Value

- **function parameter**에 입력이 없을 때 사용되는 **기본 값** 설정이 가능하다.

```cpp
int divide(int a, int b=2){
	return a/b;
}
```

## Function **Overloading**

- 동일한 함수명 but 다른 parameter list(type, 개수 다름) 사용 가능

## Function Template

- generic type function 선언 가능
    - Class에서 template을 쓰면 container

```cpp
template <class T>
void mySwap(T &x, T &y){
	T temp = x;
	x = y;
	y = temp;
}

// 아래 2가지 형태 모두 가능
mySwap<int>(intA, intB);
mySwap(intA, intB);
```

- second element
    - fixed_multiply(10, 2)와의 차이: template에 second element를 줄 경우, 해당 숫자가 들어간 새로운 함수가 각각 생김

```cpp
template <class T, int N>
T fixed_multiply (T val) {
	return val * N;
}

fixed_multiply<int,2>(10)
fixed_multiply<int,3>(10)
```