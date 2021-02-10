---
layout: post
title: XCode Simulator 화면 녹화하는 방법
comments: true
tags: [iOS,XCode]
category: [iOS]
---

📱 XCode에서 작업 중 Simulator를 녹화하고 싶다면?

Terminal을 실행하고 간단히 한줄이면 된다.

`xcrun simctl io booted recordVideo "요기에 저장하고 싶은 이름 적으세요".mov`

입력하게 되면 바로 녹화가 시작 된다.

녹화를 종료 하고 싶으면 `ctrl + c` 눌러주면 종료가 된다.

<p align = "center"><img width="573" alt="recording_simulator01" src="https://user-images.githubusercontent.com/41679458/107479732-dff0f180-6bbe-11eb-9227-b8f6933b286b.png"></p>


생각해보니 작업 중인 디렉터리로 가서 실행해야하는지..? 파일 저장 경로가 현재 디렉터리인지 시도를 해보지 않았다.

해보는데로 업데이트 할 예정!