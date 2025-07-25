---
title: "[C++] new, delete를 통한 동적 메모리 할당 및 비우기"
categories:
- C++
tags:
- C++
- memory
---

C 언어 기반의 언어들(C, C++, C#)은 기본적으로 컴파일러가 컴파일 시점에 메모리를 할당하고 사용한다.(정적 할당)

하지만 코드를 사용하다 보면, 런타임(실행 중)에 필요한 만큼의 메모리 공간을 확보할 필요가 생긴다. 이런 방식을 **동적 메모리 할당**이라고 부른다.

동적 메모리 할당에서 주의해야 할 점은 **메모리 할당 해제**이다.

정적 할당의 경우 컴파일러가 자동으로 메모리 할당 및 해제를 하기 때문에 따로 지정해줄 필요가 없지만, 동적 할당의 경우 작성자가 이를 명확히 지정해주어야 한다.

만약 동적 메모리를 할당한 후, 해제를 명시하지 않을 경우, **해당 부분 코드가 실행될 때 마다 메모리에 공간을 추가로 할당** 받게 된다. 이것이 누적되면 메모리 에러로 이어지게 된다.

따라서 이런 문제가 생기지 않도록, 할당된 모든 동적 변수를 사용 후엔 반드시 할당 해제하도록 주의를 기울여야 한다.

C언어의 기본적인 동적 메모리 할당 방법은 `malloc`과 `free`를 사용하는 것이다.

하지만 C++에서는 `new`와 `delete`라는 새로운 방식이 도입된다.

훨씬 쉽고 깔끔하게 사용할 수 있기 때문에, C++ 사용자라면 new와  delete를 사용하기를 권장한다.

## 기본 사용법 - new, delete

### 메모리 할당하기(new)

c++에서 동적 메모리를 선언하는 것은 매우 간단하다.

`new`를 붙여서 object를 선언한 후, **포인터**에 넣어주면 된다.

```bash
int* a = new int(1);
```

위 구조에서 int 자리에 class나 struc을 포함한 원하는 자료형을 넣으면 된다.

### 메모리 할당 해제하기(delete)

동적 메모리 할당에서 주의해야 할 부분은 할당 해제 부분이다.

기본적으로 동적 할당된 메모리를 해제하는 방법은 아래와 같이  `delete` 를 사용하는 것이다.

```bash
delete a;          # 비우기
```

기본적인 방식은 위와 같이 간단하지만, 실제 사용할 때는 생각보다 번거롭게 사용되기도 한다.

이때의 해제하는 방식 예제들을 소개한다.

## 리스트 할당 및 해제

- 할당

```bash
int* a = new int[5];
```

- 해제

```bash
delete[] a; # 리스트 비우기
```

## 순환 객체 할당 및 해제 (ex. vector, unordered_map)

### 전체 삭제

크기를 특정할 수 없는 대부분의 기타 iterable 객체 속에 동적 객체를 선언했을 경우, 

해당 객체가 없어지기 전에 반드시 반복문을 돌면서 하나씩 메모리를 비워야한다.

- vector를 예로 들면 아래와 같다.

```bash
using namespace std;

# 할당
vector<float*> nodes;
nodes.push_back(new float(1.0));

# 해제
for_each(nodes.begin(), nodes.end(), [](auto& node) {delete node; })
```

- unordered_map 다른 순환 객체들도 마찬가지 방식으로 하나 씩 비워 주어야 한다.
- 반복문의 형식은 위와 같을 필요는 없다. 각 요소들을 돌면서 각각 다 비워주기만 하면 된다.

### 특정 동적 원소 지우기

위에서와 같이 `vector <obejct *>` 구조로 선언하였을 때, 해당 벡터를 통채로 지우는 것보다 까달로운 경우는 이 중 특정 한 원소만 지우는 경우이다.

위에서는 해당 vector를 더 이상 사용하지 않는다는 가정이므로, 그냥 원소만 할당 해제하면 된다. 하지만 해당 벡터는 사용하고, 그 속 원소만 지우는 경우에는 조금 더 복잡해진다.

이때는 

1. vector에서 해당 원소 위치 찾아서 삭제 (해당 원소가 뭔지 기억)
    1. vector에서 특정 원소의 위치를 지우는 방법을 구체적으로 이해하고 싶으면, [[C++] vector에서 특정 객체 삭제하기(remove, erase 차이 및 사용법)](%5BC++%5D%20vector%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5%20%E1%84%90%E1%85%B3%E1%86%A8%E1%84%8C%E1%85%A5%E1%86%BC%20%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%20%E1%84%89%E1%85%A1%E1%86%A8%E1%84%8C%E1%85%A6%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(remove,%20er%201110d37911fa802f8945d80c853dd312.md) 를 참고하자.
2. 해당 원소 delete

순서로 진행하여야 한다.

```python
nodes.erase(remove(nodes.begin(), nodes.end(), nodeA) nodes.end();
delete nodeA;
```

만약 삭제하고자 하는 노드를 인덱스로 알고 있다면, 아래처럼 주소를 저장하는 과정을 해야 한다.

인덱스로 바로 원소를 삭제하면 그 원소를 가리키는 포인터가 삭제되어, delete 할 수 없어지기 때문이다. 따라서 아래 과정을 통해 삭제한다.

```python
float* nodeA = nodes[i];
nodes.erase(remove(nodes.begin(), nodes.end(), nodeA) nodes.end();
delete nodeA;
```

## Custom 객체 속 동적 할당 및 해제 - Constructor(생성자) & Destructor(소멸자)

자료형을 만들면서 내부에 동적 객체를 사용하고자하는 경우에는

소멸자에 동적 객체를 모두 비우도록 설정해주는 것이 좋다.

생성자에서 동적 객체를 선언하는 경우 뿐만 아니라, 해당 객체를 사용하면서 생성될 모든 동적 객체를 고려해서 소멸자에 넣는 것이다.

예를 들면 아래와 같다.

```python
Grid::~Grid(){
	delete edge;
	for (int i=0; i<len(nodes); i++){
		delete nodes[i];
	}
}
```

이를 통해 해당 객체가 할당 해제될 때, 자동으로 내부의 동적 객체들도 할당 해제되게 된다. 이를 통해 메모리에 누적되는 오류를 피할 수 있다.

## 참고자료

- https://velog.io/@saint6839/C언어-동적-메모리-할당-개념-잡기
- [https://jeckl.tistory.com/entry/C-23강-메모리-동적할당-new-delete](https://jeckl.tistory.com/entry/C-23%EA%B0%95-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EB%8F%99%EC%A0%81%ED%95%A0%EB%8B%B9-new-delete)
- [https://velog.io/@cse_pebb/C-remove-함수-vs.-vector의-erase-함수](https://velog.io/@cse_pebb/C-remove-%ED%95%A8%EC%88%98-vs.-vector%EC%9D%98-erase-%ED%95%A8%EC%88%98)
- [https://www.notion.so/C-vector-remove-erase-1110d37911fa802f8945d80c853dd312?pvs=4](%5BC++%5D%20vector%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5%20%E1%84%90%E1%85%B3%E1%86%A8%E1%84%8C%E1%85%A5%E1%86%BC%20%E1%84%80%E1%85%A2%E1%86%A8%E1%84%8E%E1%85%A6%20%E1%84%89%E1%85%A1%E1%86%A8%E1%84%8C%E1%85%A6%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5(remove,%20er%201110d37911fa802f8945d80c853dd312.md)