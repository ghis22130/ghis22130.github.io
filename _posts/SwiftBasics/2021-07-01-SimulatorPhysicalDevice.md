---
layout: post
title: iOS Simulator vs Physical iOS Device
comments: true
tags: [OS, DB, MySQL, Docker]
category: [SwiftBasics]
---

실제 기기에서만 테스트 할 수있는 환경들이 있다.

언제 포스팅 된 글인지는 모르겠지만 Push Notifications같은 경우 [Xcode 11.4](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_4-release-notes) 부터 [Remote Push Notifications](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) 를 지원한다고 한다!

<p align = "center"><img src = "/assets/img/Swift_img/SimulatorDevice01.png"></p>



차이점을 정리해보면.. 

- 카메라

- System Testing (background, foreground) 

  > 테스트 할 수 있는 것 같다는 생각이 들지만 ...

- Hardware functionality (Bluetooth, GPS, 근접센서 .. 각종센서 등등)

- 오디오 입력

- 앱 퍼포먼스 테스팅 ( feat 여러 프레임 워크들 )

- openGL ES 

  > 무슨 기능을 하는지 찾아보자

- 실제 사용자의 100% 환경

  

정도 되는것 같다 참고로 실제 개발 코드로 simulator와 physical device를 구분해서 구현해주어야 한다면



```swift
#if targetEnvironment(simulator)
  // Simulator
#else
  // Device
#endif
```

혹은

```swift
if TARGET_IPHONE_SIMULATOR == 1 {
  // Simulator
} else {
  // Device
}
```

로 구분해서 구현해줄 수 있다.



## 참고사이트

[https://www.browserstack.com/test-on-ios-simulator](https://www.browserstack.com/test-on-ios-simulato)

[https://lidium.tistory.com/44](https://lidium.tistory.com/44)

[https://woongsios.tistory.com/126](https://woongsios.tistory.com/126)

