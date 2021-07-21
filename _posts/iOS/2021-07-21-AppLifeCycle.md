---
layout: post
title: AppLifeCycle
comments: true
tags: [iOS,XCode]
category: [iOS]
---

iOS 애플리케이션은 5가지의 상태를 가지고 있다.

- **Not Running**
  - 앱이 실행 되지 않았거나 완전히 종료되었을 때
- **In-active**
  - 앱이 실행되면서 Foreground에 진입하지만 어떠한 이벤트도 받지 않는 상태 (ex Launch Screen)
- **Active**
  - 앱이 실행 중이며 Foregound에 있고 이벤트를 받고 있는 상태
- **Background**
  - 앱이 Background에 있으며 다른 앱으로 전환되었거나 홈 버튼을 눌러 밖으로 나갔을 때 상태
- **Suspended**
  - 앱이 Background에서 특별한 작업이 없으면 전환되는 상태



<img align = "center" src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FHOlZG%2FbtqLpSPYXIk%2Fv5Cyv6iAkQ4dGSAxgrvvx0%2Fimg.png">

---

#### **Not Running**

**[application(_:willFinishLaunchingWithOptions:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application)**

앱 실행을 준비하는 메소드.

필요한 주요 객체들을 생성하고 앱 실행 준비가 끝나기 직전에 호출된다.

 

**[applicationDidFinishLaunching(_:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623053-applicationdidfinishlaunching)** 

앱 실행을 위한 모든 준비가 끝난 후 화면이 사용자에게 보여지기 직전에 호출된다.

초기화 코드를 주로 이곳에다 작성.

 

**[applicationWillTerminate(_:)](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623111-applicationwillterminate)**

앱이 종료되기 직전에 호출된다.

(하지만 메모리 확보를 위해 suspended 상태에 있는 앱이 종료될 때나 background 상태에서 사용자에 의해 종료될 때나

오류로 인해 앱이 종료될 때는 호출되지 않는다.)

 

**In-Active**

 

**[sceneWillEnterForeground(_:)](https://developer.apple.com/documentation/uikit/uiscenedelegate/3197918-scenewillenterforeground).**

앱이 백그라운드나 낫러닝에서 포어그라운드로 들어가기 직전에 호출.

비활성화 상태를 거쳐 활성화 상태가 된다.

 

**[sceneWillResignActive(_:)](https://developer.apple.com/documentation/uikit/uiscenedelegate/3197919-scenewillresignactive)**

사용자가 Scene과의 상호작용을 중지할 때 호출된다.

(다른 화면으로 이동할 경우)

 

 

**Active**

**[sceneDidBecomeActive](https://developer.apple.com/documentation/uikit/uiscenedelegate/3197915-scenedidbecomeactive)[(_:)](https://developer.apple.com/documentation/uikit/uiscenedelegate/3197915-scenedidbecomeactive)**

앱이 In-active에서 Active로 진입하고 난 직후 호출됨.

앱이 실제로 사용되기 전에 마지막으로 준비할 수 있는 코드를 작성할 수 있다.

 

**Background** 

**[sceneDidEnterBackground(_:)](https://developer.apple.com/documentation/uikit/uiscenedelegate/3197917-scenedidenterbackground?language=objc)**

앱이 백그라운드 상태로 들어갔을 때 호출된다.

suspended 상태가 되기 전 중요한 데이터를 저장하는 등 종료하기 전에 필요한 작업을 한다.

 

**Suspended** 

따로 호출되는 메소드는 없다.





---

[참고](https://fomaios.tistory.com/entry/%EC%95%B1-%EC%83%9D%EB%AA%85%EC%A3%BC%EA%B8%B0App-LifeCycle-1)

