---
title : "[c++] Stream 입출력 & Buffer"
categories:
- c++
tags:
- c++
---

- C++은 stream class을 통한 in/out을 제공한다.

## User IO

```cpp
#include <iostream>
std::cin >> num;
std::cout << “Hello C++!” << std::endl;
```

- 특징 : characters가 queue구조로 순차적으로 in/out
- 요소
    - cout : 화면 출력 대기
    - cin : 키보드 입력 대기, space 단위로 끊어서 인식
    - << : 오른쪽 string을 왼쪽에 넣기
    - >> : 왼쪽 결과를 string에 넣기 & 오른쪽 변수에 맞춰 type 변경.
    - endl : 줄바꿈(\n) & 화면에 flush
- getline
    
    ```cpp
    #include <iostream>
    #include <string>
    getline(std::cin, myStr);
    ```
    
- **stringstream**
    - **string을 stream처럼 취급**
    - **자동 type 변환**이 가능해짐
    
    ```cpp
    #include <sstream>
    stringstream(myStr) >> myInt;
    ```
    

## File IO

- 종류
    - ofstream : write on file
    - ifstream : read from file
    - fstream : both read and write from/to files
- mode
    
    
    | ios::in | input(reading) |
    | --- | --- |
    | ios::out | output(writing) |
    | ios::binary | binary file로 연다.(이게 없으면 text로 읽음)
    음악 파일들에서 주로 사용. |
    | ios::ate | 파일의 마지막 부분을 시작점으로 |
    | ios::app | ios::out일 때, 매번 writing 할 때마다 파일 맨 뒤로 계속 이동(overriding 방지) |
    | ios::trunc | ios::out일 때, 파일 열 때 기존 내용 모두 삭제 |
    - default mode
    
    | ofstream | ios::out |
    | --- | --- |
    | ifstream | ios::in |
    | fstream | ios::in | ios::out |
- 기본 틀
    
    ```cpp
    #include <iostream>
    #include <fstream>
    using namespace std;
    
    int main(){
    	// 선언 후 open
    	ofstream myfile;
    	myfile.open(파일명, 모드);
    
    	if (myfile.is_open()){                        // 이건 필수 아님
    		... //기능 넣기
    		myfile.close();                             // 닫기
    	}else{
    		cout << "Unable to open file";
    	}
    	return 0;
    }
    ```
    
- constructor로 선언도 가능
    
    ```cpp
    //위 main에서 첫 두 줄을 아래 한 줄 constructor로 대체 가능
    ofstream myfile (파일명, 모드);
    
    // 예시 : ofstream myfile (파일명, ios::out | ios::app | ios::binary)
    ```
    
- 기능
    
    ```cpp
    #include <string>
    string line;
    
    //write
    myfile << "This is a line.\n";
    //read
    while(getline(myfile, line)){ cout << line <<'\n';}
    
    //binary read (write도 가능)
    streampos size;                    // file이나 buffer에서 위치를 나타내는 
    size = file.tellg();               // 파일에서 get이라는 pointer의 현위치. streampos type return
    memblock = new char [size];        // memblock 이라는 pointer가 가리키는 곳에 size 만큼의 공간 만들기
    file.seekg (0, ios::beg);          // get pointer가 ios::beg위치로부터 0만큼 떨어진 곳을 가리키게 됨.
    file.read(memblock, size);         // size만큼 읽어서 memblock에 저장
    
    ```
    
- 형식 변환
    - getline등은 char로 불러온다.
    - 따라서 필요한 type으로 변환 필요
    
    ```cpp
    std::stoi(line); // string -> int
    std::stod() //  string -> double
    std::stold() // string -> long double.
    ```
    

## Buffer & Synchronization

- buffer는 fileIO, 통신, 동영상 재생 등 data 이동이 있으면 늘 필요하다.
    - buffer 없으면 한순간 잘못 입력한 것도 바로 다 출력되어, 안정성이 떨어진다.
- buffer object : type `streambuf`
- Synchronization
    - buffer를 비우고, 그 속이 있는 모든 걸 출력
    - 외부/내부 괴리가 없어짐
    - 대표적 예 : std::flush, std::endl