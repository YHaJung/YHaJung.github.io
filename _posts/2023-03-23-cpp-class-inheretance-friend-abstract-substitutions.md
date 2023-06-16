---
title : "[C++] class간의 특수관계 및 특징 : inheretance, friend, abstract, substitutions"
categories:
- c++
tags:
- c++
---

## 1. Friend Class

- C가 friend로 지정해둔 class는 C의 private, protected member까지 모두 접근 가능하다.
- 단, 일반향 선언이다. 쌍방향을 원하면 상대로 friend로 지정해야 한다.

```cpp
class Square{
	friend class Rectangle;
	private:
		int side;
};  

void Rectangle::convert(Square a){
	width = a.side;
	height = a.side;
}
```

## 2. Abstract Class

- **인스턴스화(object 생성)할 수는 없지만** 상속될 수 있는 Class
- 하나 이상의 **method가 Pure Virtual**이면 Abstact Class이다.
    - `=0` 혹은 `=NULL`로 선언된 `virtual` method
        
        ```cpp
        virtual void EndMonth(void) = NULL
        ```
        

## 3. 상속(Inheritance)

- 기존 클래스를 가져와서, **새로 추가되는 부분만 구현**한다.
- 재사용성이 생긴다.
- 트리와 같은 구조로 표현할 수 있다.
- 마크 : `:`

```cpp
// class 상속
class Mommabear : public Bear {
}
```

### a. **Access Specifier in Inheritance**

- 상속하는 Class 앞 Access Specifier로, 부모 클래스 속 accessibility를 바꿀 수 있다.
- 원래 정의된 accessibility와 상속하며 붙인 access specifier 중 **보안 정도가 강한 것으로** 적용된다.
- Access Specifier : public, protected, private(default)

### b. Binding

- object가 message를 받으면 해당하는 method가 호출되는 것을 의미한다.
- message는 호출된 클래스에서 시작해서 부모 클래스들로 타고 올라가며(travel-up), 처음 만나는 method를 binding한다.
- 종류
    - static binding
        - 일반적인 케이스.
        - compile time에 binding한다.
    - dynamic binding
        - `virtual` keyword가 사용될 때
        - run time에 binding
        - 대역(substitution)이 사용되었을 때 필요하다. compile time에는 포인터가 부모 클래스를 가리키고 있지만, runtime에 대역인 자식 클래스 object가 생성되어 override 했을 수 있기 때문이다.

### c. Multiple parents

- 여러 부모를 동시에 상속할 수 있다.

```cpp
class Triangle: public Polygon, public Output {
	...
}; 
```

### d. **Class Substitutions(대역)**

- 자식 클래스는 부모 클래스의 대역이 될 수 있다.
- 즉, 부모 클래스로 선언한 object에 자식 클래스를 넣을 수 있다.
- 그 역은 성립하지 않는다.

### e. 상속 불가능한 Class Memebers

- constructor, destructor
- operator member
- friend class
- private members
    - private data의 경우, 상속은 되어 자식 object의 메모리에 존재하나 접근할 순 없다.

### f. Parent’s constructor, destructor calling

- constructor와 destructor 의 경우, 상속되진 않지만 자동으로 부모&조상 클래스들의 constructor와 destructor를 호출한다.
- 상속으로 합쳐지는 것이 아니라, 각각 순차적으로 모두 부르는 것이다.
- 부르는 순서
    - constructor : 조상 → 부모 → 자식
    - destructor : 자식 → 부모 → 조상
- 부모 클래스의 constructor들이 여러 개일 경우, initialization list를 통해 지정할 수 있다.
    
    ```cpp
    class Son : public Mother {
    	public:
    		Son (int a) : Mother (a) { cout << "Son: int parameter\n\n"; }
    };
    ```
    
    - 지정하지 않을 경우, argument가 없는 default constructor가 호출된다.
        - 만약 부모 class에 default constructor가 없으면 error 발생
- 자식 class의 constructor가 parent가 아닌 할아버지 클래스의 constructor를 직접 호출할 수는 없다.