---
title : "[c++] Type 확인 및 변환"
categories:
- c++
tags:
- c++
---

- C++은 C보다도 더 strong-typed language이다.
    - 즉, 프로그래머가 아는 type에서 다른 type으로 프로그램이 자체 변형하는 경우가 잘 없다.

### 현재 타입 확인 : typeid

```cpp
#include <typeinfo>
typeid(a)
cout << typeid(a).name() << endl;
```

## Type 변환

### Stream을 이용한 type 변환

- Stream은 기본적으로 자동 타입 변환 기능이 있다. 이를 이용해, string을 stream으로 바꿔서 type 변환을 할 수도 있다.
- **stringstream**
    - **string을 stream처럼 취급**
    - **자동 type 변환**이 가능해짐
    
    ```cpp
    #include <sstream>
    stringstream(myStr) >> myInt;
    ```
    

### std 변환

```cpp
std::stoi(line); // string -> int
std::stod() //  string -> double
std::stold() // string -> long double.

std::atof() // char array-> double

std::to_string(num_float);  // float, double -> string
```

### Type Casting 변환

- 변환 실패 시 nullptr 반환
- 종류
    - dynamic_cast
        - 변환될 타입이, 포인터가 가리키고 있는 실제 object의 type과 일치해야 함
        - 하나 이상의 virtual function을 가진 pointer 함수만 가능
        - type safety check는 runtime에
        
        ```cpp
        Base* a = new Derived;
        c = dynamic_cast<Derivated*>(a);
        ```
        
    - static_cast
        - 서로 관련된 type끼리만 가능
            - 부모 클래스 ↔ 자식 클래스
            - 숫자 끼리
        - type safety check는 compile time에
        
        ```cpp
        Base *a = new Base();
        Derived *b = static_cast<Derived*>(a);
        
        int a=10;
        double b = static_cast<double>(a);
        ```
        
    - reinterpret_cast
        - 관련 없어도 억지로 변환
        - 통신 직전/직후에 주로 사용
        - dynamic_cast, static_cast 등에선 bit값 자체가 바뀌지만, 이건 bit 상태를 유지하며 type만 강제 변환한다.
        
        ```cpp
        B*b = reinterpret_cast<B*>(a);
        ```
        
    - const_cast
        - constness ↔ non-constness 변환
            - const : 상수
        - 용도
            - const 선언 했지만, param으로 보내며 일시적인 해제가 필요한 등 경우
            - C → C++ 변환 때 호환을 위해 많이 사용
        
        ```cpp
        const_cast<char *>(c);
        ```