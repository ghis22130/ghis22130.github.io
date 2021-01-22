---
layout: post
title: Process 와 Thread
comments: true
tags: [OS, Process, Thread]
category: [ComputerScience]
---

대학교 운영체제 시간에 배웠던 개념들이라 다시 접하는데 크게 거부감이 들지는 않았지만 오랜만에 다시 보는 용어들에 어렴풋한 기억들로 정확한 정의가 떠오르지 않았다.



Process와 Thread의 개념을 다시한번 스스로 정의해보는 시간을 가지고 추가 학습을 해보려 한다.



## 프로그램? 프로세스?



<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FWxFTY%2FbtqzNBGy35r%2FbVdhmxQT1zHYNF2uFo8kGK%2Fimg.png" width="350px">

### 프로그램

☝️ 디스크에 저장되어있는 일련의 명령어들의 집합

✌️ 프로그램은 보조 기억장치(하드디스크, SSD)에 존재하며 실행되기를 기다리는 명령어(코드)와 정적인 데이터의 묶음



### 프로세스

☝️ 프로그램이 **메모리(DRAM)** 에 적재되어 **실행** 중인 프로그램이 프로세스이다.

✌️ 프로그램을 구동하여 프로그램 자체와 프로그램의 상태가 메모리 상에서 실행되는 작업 단위를 지칭 

------------------------------------

❗️프로그램은 실행중이지 않은, 동작되고 있지 않은 **정적인 개체**, 프로세스는 실행중이기 때문에 **동적인 개체**



## 프로세스 메모리 구조

프로세스가 메모리에 **locate** 될 때 구조는 다음과 같다.

<img src = "http://public.codesquad.kr/jk/cs23/step2-memorymodel.png" width = "60%">

<img src ="http://public.codesquad.kr/jk/cs23/step2-stackvariable_heap.png">

- <span style="color:#1C4C71">**스택(stack)**</span> : 함수나 프로시저를 호출하고 리턴할 때 복귀 주소나 지역 변수와 같은 일시적인 데이터를 저장하는 메모리 영역이다.
- <span style="color:#1C4C71">**힙(heap)**</span> : 프로그램 실행 중에 동적으로 메모리를 할당할 수 있는 자유로운 영역이다.
- <span style="color:#1C4C71">**데이터(BSS, GVAR)**</span> : 초기화한 데이터 구조에 따라서 읽고 쓰기가 가능한 영역이다.
- <span style="color:#1C4C71">**텍스트(text)**</span> : 프로세서가 실행할 바이너리 코드를 저장해 놓은 영역이다.

### 프로세스의 상태

 ✔️ [커널](https://ko.wikipedia.org/wiki/커널_(컴퓨팅)) 내에는 준비 큐, 대기 큐, 실행 큐 등의 [자료 구조](https://ko.wikipedia.org/wiki/자료_구조)가 있으며 커널은 이것들을 이용하여 프로세스의 상태를 관리한다.

<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Process_states.svg/1920px-Process_states.svg.png" width = "50%">

- <span style="color:#1C4C71">**생성(create)**</span> : 프로세스가 생성 되는 중이다

- <span style="color:#1C4C71">**실행(running)**</span> : 프로세스가 **CPU**를 차지하여 명령어들이 실행되고 있다.
- <span style="color:#1C4C71">**준비(ready)**</span> : 프로세스가 CPU를 사용하고 있지는 않지만 언제든지 사용할 수 있는 상태로, CPU가 할당되기를 기다리고 있다. 일반적으로 준비 상태의 프로세스 중 우선순위가 높은 프로세스가 CPU를 할당받는다. (_스케줄링 알고리즘_)
- <span style="color:#1C4C71">**대기(wating)**</span> : 프로세스의 실행이 종료되었다



## 프로세스의 상태전이

<img src = "https://wiki.kldp.org/pds/ProcessManagement/state_diagram.jpg" width ="50%">

✔️ 하나의 프로그램이 **실행**되면 그 프로그램에 대응되는 프로세스가 **생성**되어 준비 리스트의 끝에 들어간다.

✔️준비 리스트 상의 다른 프로세스들이 CPU를 **할당**받아 준비 리스트를 떠나면, 그 프로세스는 점차 준비 리스트의 앞으로 나가

​     게 되고 언젠가 CPU를 **사용**할 수 있게 된다.

- <span style="color:#1C4C71">**디스패치(dispatch)**</span> : 준비 리스트의 맨 앞에 있던 프로세스가 CPU를 점유하게 되는 것, 즉 준비 상태에서 실행 상태로 바뀌는 것을 디스패치라고 하며 다음과 같이 표시한다.

  ```
  dispatch (processname) : ready → running
  ```

- <span style="color:#1C4C71">**보류(block)**</span> : 실행 상태의 프로세스가 허가된 시간을 다 쓰기 전에 입출력 동작을 필요로 하는 경우 프로세스는 CPU를 스스로 반납하고 보류 상태로 넘어 간다. 이것을 보류라고 하며 다음과 같이 표시한다.

  ```
  block (processname) : running → blocked
  ```

- <span style="color:#1C4C71">**깨움(wakeup)**</span> : 입출력 작업 종료 등 기다리던 사건이 일어났을 때 보류 상태에서 준비 상태로 넘어가는 과정을 깨움이라고 하며 다음과 같이 표시한다.

  ```
  wakeup (processname) : blocked → ready
  ```

- <span style="color:#1C4C71">**시간제한(timeout)**</span> : 운영체제는 프로세스가 프로세서를 계속 독점해서 사용하지 못하게 하기 위해 clock interrupt를 두어서 프로세스가 일정 시간동안만 (시분할 시스템의 time slice) 프로세서를 점유할 수 있게 한다

  ```
  timeout(processname) : running -> ready
  ```



## PCB(Process Control Block)

공부하자..!



## Thread(스레드)

✔️ **스레드**(thread)는 어떠한 프로그램 내에서, 특히 프로세스 내에서 실행되는 흐름의 단위를 말한다. 

✔️ **경량 프로세스 Light Weight Process**라고 프로세스에서 실행 제어만 분리해서 처리하는 단위를 만들었다.

✔️ 스레드는 같은 그룹의 스레드와 코드, 메모리 주소 공간, 운영체제 리소스를 공유한다. 프로세스는 하나 이상의 스레드를 가지

​     고 각 스레드는 다음 같은 동작을 담당한다.



- 스레드 실행에 대한 상태 관리
- 실행을 위한 별도 스택
- 지역 변수와 스레드 특정 데이터를 저장하는 데이터 저장소
- 프로세스의 메모리와 자원에 대한 접근을 기록하는 컨텍스트 정보

<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Multithreaded_process.svg/440px-Multithreaded_process.svg.png" width="50%">



### 특징

- 스레드를 사용하면 사용자에 대한 응답성을 증가시킬 수 있다.
- 프로세스 자원과 메모리를 공유할 수 있다.
- 자원을 공유하기 때문에 경제적이다.
- 다중 프로세서와 다중 스레드를 혼합해서 병렬 실행이 가능하다.
- 현대 CPU들은 다중 스레드를 처리하는 하드웨어 로직을 가지고 있다



## 멀티프로세스? 멀티스레드?

멀티프로세스와 멀티스레드는 양쪽 모두 여러 흐름이 동시에 진행된다는 공통점을 가지고 있다.

차이점은 무엇일까?



### 멀티 프로세스 (Multi Process)

