---
title : "[C++] Class Template : Container & STL(vector, set, map, list)"
categories:
- c++
tags:
- c++
---

## Container란?

- Class Template
- 아무 타입이나 넣을 수 있는 class data structure

```cpp
template <class T>
class myPair {
	T values [2];
	public:
	myPair (T first, T second){
		values[0] = first;
		values[1] = second;
	}
};
myPair<int> myObject (115, 36);
myPair<double> myFloats (3.0, 2.18);
```

- Container class 속의 method를 template으로 정의할 수도 있다.

```cpp
template <class T>
class myPair {
	...
	T getMax ();
};

template <class T>
T myPair<T>::getMax () {
	T retval;
	retval = a>b? a : b;
	return retval;
}

myPair <int> myObject (100, 75);
cout << myObject.getMax();         // obj에서 지정한 template type이 method에도 그대로 적용됨
```

## C++ Standard Template Library (STL)

- C++에 기본 구현되어 있는 유용한 Container들
- dynamic data structure
    - heap에 저장
    - vector에 원소 추가 시, 통째로 이사(array 특유의 연속성은 유지하며 dynamic하게 공간확보 위함)
- 대표 종류
    
    
    | C++ Equivalent <br> (container) | Data structure in Python | Characteristics |
    | --- | --- | --- |
    | vector  | list  | A dynamic ordered list |
    | unordered_set  | set  | A dynamic set of unordered unique values |
    | unordered_map  | dictionary  | A dynamic set of (key-value) pairs |
    | list  | deque  | A doubly linked list |
- I**nitialization** (Vector 기준)
    - vector 이외에도 형식 동일
    
    |||
    | --- | --- |
    | vector<int> a; | a is an empty dynamic array object that can hold integers |
    | vector<int> a{10, 20}; | a is a dynamic array object that contains 10 and 20 |
    | vector<int> a(5); | a is a dynamic array object that contains five elements |
    | vector<int> a(5,10); | a is a dynamic array object that contains five 10s |
- **Methods** (Vector 기준)
    - vector 이외에도 형식 동일
    
    |||
    | --- | --- |
    | a.front();  | Return the first item |
    | a.pop_front();  | Remove the first item |
    | a.push_back(5);  | Add a new item at the end |
    | a.back();  | Return the last item |
    | a.pop_back();  | Remove the last item |
    | a.empty();  | Return true if the vector is empty |
    | a.size();  | Return the number of items |