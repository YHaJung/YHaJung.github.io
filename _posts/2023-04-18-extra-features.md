---
title : "[C++] 기타 기능들 : String, Exception, Range, Namespace"
categories:
- c++
tags:
- c++
---

## Exceptions

- 예외적 상황에 반응
    - ex) runtime errors
- 형식 : try-catch block

```cpp
try{
	//문제 있으면 throw keyword
}
catch (int param) { }
catch (const std::exception& e){ }
```

- Standard Exception
    - exception 종류를 모아둔 library
    - std::exception
    
    ```cpp
    #include <exception>
    class myException : public exception{
    	virtual const char* what() const throw(){
    		return "My exception happend";	
    	}
    } myex;
    ```
    
    - what() : 지금 해당하는 exception이 뭔지 print하기 위한 구문.
    - const throw() : 이 함수는 어떤 exception도 throw하지 않을 거라는 안정 보장해주는 specifier.
        - 위 예에선 어차피 print만 해서 당연
        - exception 핸들링 하려고 만들었는데 exception 만들어내면 이상

## string 사용법

```cpp
#include <iostream>
#include <string>
std::string myStr;
```

## **Range**-based for loop

- range : a sequence of elements

```cpp
for (char c : myStr){
	cout << c;
}
```

- **auto** type : 들어오는 sequence에 따라 자동으로 type 지정 가능

```cpp
for (auto c : myStr){
	cout << c;
}
```

## Namespace

- 목적 : library간의 naming conflict 문제 해결
- namespace 범위 안에서 작동하여, 그 안에서만 unique하면 된다.
- global namespace는 defualt라 입력하지 않아도 됨. 하지만 나머지는 입력 필수.
- 정의법
    
    ```cpp
    namespace foo{
    	const double pi = 3.1416; // 상수	
    	double value(){           // 함수
    		return 2*pi;            // 동일 namespace에서 참조할 땐 std 안 붙여도 됨
    	}
    }
    namespace foo{              // 이렇게 분리되서 정의해도 됨. 위와 아래 둘 다 동작.
    	int a;
    }
    ```
    
- namespace 사용법 : scope operator(::)를 쓴다.
    
    ```cpp
    std::cout //std라는 namespace 속으로 들어가서 cout 찾기
    
    using foo::pi;            // 이 이후론 foo::없이 pi 사용가능 
    std::cout << pi << '\n';
    
    using namespace std;      // 이 이후론 std:: 없어도 std 속 모든 것 사용 가능
    	                        // std namespace 많이 사용되어, 미리 using하는 경우 많음.
    
    {                         // block 속에서만 using 작동
    	using namespace pi;
    }
    ```
    
- namespace 이름 바꾸기
    
    ```cpp
    namespace new_name = current_name;
    ```