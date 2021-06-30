---
layout: post
title: Frame vs Bounds
comments: true
tags: [OS, DB, MySQL, Docker]
category: [SwiftBasics]
---

UIView 관련된 객체들을 다루다 크기에 대한 정보를 얻기위해선 frame, bounds 를 마주하게 된다.


<p align = "center"><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbe5D6m%2FbtqLRklY2Cc%2FbBwGjCKKF2kekLjxHtNdw1%2Fimg.png"></p>



둘 다 기본적으로 위치(Origin) 와 크기(Size)를 가지고 있다. 



**둘의 차의점**

<p align ="center"><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FekJFKT%2FbtqLRlcTsNm%2FfmDGW2QjejfD2S8KUOIn61%2Fimg.png"></p>

**Super View 좌표계**에서 **View의 위치와 크기**를 나타낸다

즉 Super View에서 해당 View를 감싸는 영역을 사각형으로 나타낸 것이다. 



<p align = "center"><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FblGhmq%2FbtqLTyLWYgT%2FkTzbqxNij5BkGmnHNNF0x1%2Fimg.png" width = "60%"></p>

위와 같이  View가 회전 되어있지 않다면 frame과 bounds의 width 와 height는 동일할 것이지만

<p align = "center"><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcG2Tof%2FbtqLRU2vVaV%2Funr8fQGs3Ts7vW6TYqRf81%2Fimg.png" width = "60%"></p>

위 와 같이 View가 회전 하게 된다면 frame은 뷰를 감싸는 사각형의 영역을 표시하게 되기 때문에 width와 height가 변하게 된다.



그렇다면 bounds는? 

<p align = "center"><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FsHDbf%2FbtqLWHA5Ffw%2FO1Kp67kTBWGQC5Q99fHe20%2Fimg.png"></p>

**자신의 좌표계** 에서 View의 위치와 크기를 가지게 된다.

즉 자신이 회전을 하든 뭐를 하든 고유한 width와 height를 가지고 있게 된다.


---

지금은 size에 대해서만 frame과 bounds를 다루어 보았지만 가장 중요한 차이점인

어느 좌표계를 기준으로 하냐만 이해할 수 있다면 origin에 대한 로직도 이해할 수 있을 것이다.

- 참고 사이트 : [https://babbab2.tistory.com/44?category=831129](https://babbab2.tistory.com/44?category=831129)