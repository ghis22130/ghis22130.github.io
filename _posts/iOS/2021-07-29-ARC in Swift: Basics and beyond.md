---
layout: post
title: ARC in Swift Basics and beyond
comments: true
tags: [iOS,XCode]
category: [iOS]
---

[WWDC2021 - ARC in Swift: Basics and beyond ](https://developer.apple.com/videos/play/wwdc2021/10216/) 영상을 토대로  ARC의 역할과 설계 방향에 대해 공부해봤습니다.



영상에 대한 이야기로 넘어가기 직전 간단히 ARC에 대해 소개한다면

기본적으로 ARC는 Swift 에서 객체에 대한 참조 카운트를 계산해주고 0이 되었을 때 자동으로 메모리 해제를 해주는 아주 효자 같은 녀석입니다!



이 기능은 Obj -C 에서 MRC (Manual Refrence Counting) 메모리 관리를 더욱 편하게 성장 시켰다고 볼 수 있는데요 잠시 옵씨의 `retain` , `release` 를 이용한 객체의 생성 과정을 보면



```objective-c
- (void)setName:(NSString *)newName {
  [newName retain];
  [name release];
  name = newName;
}
```

newName을 생성 해서 retain counting을 증가시켜 객체 유지 되는 것을 보장 해준다음 기존 name에서 newName으로 옮겨가야 하니 기존에 name이 참조하고 있는 객체의 retain count를 `realease` 로 감소 시켜줍니다. ( 이때 retain count가 0 이면 deallocate)



그런데 ARC (Auto Refrence Counting)는 이러한 과정을 컴파일 단계에서 자동으로 `retain`, `release` 코드를 삽입해서 객체들의 메모리 관리를 도와줍니다!



자! 이제 WWDC 2021의 ARC 파트에 대해서 얘기해보도록 하겠습니다.



```swift
class Traveler {
    var name: String
    var destination: String?
}

func test() {
    let traveler1 = Traveler(name: "Lily")
    let traveler2 = traveler1
    traveler2.destination = "Big Sur"
    print("Done traveling")
}
```



영상의 예시 코드인데요. Traveler란 class가 존재하고 ( 기본적으로 클래스, 클로져 등 참조형 자료들이 머무는 힙영역을 HeapObject라는 구조체로 관리합니다. ) 이를 활용한 test 함수가 보이네요.



traveler1의 생성과 소멸 과정을 살펴보겠습니다.

<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdMjaZL%2Fbtq8Nvku19Q%2FmO2xumv7ywvqSXKY0NJHkk%2Fimg.png">

<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc1ixlD%2Fbtq8PuFofix%2FXgUxKcsoDoMaMBT2hgnrT1%2Fimg.png">

```swift
let traveler2 = traveler1
```

을 마지막으로 traveler1이 마지막으로 사용되면서 컴파일 단계에서 release 시켜주는 코드를 추가 시켜 주게 됩니다.

traveler1의 생성과 소멸을 살펴보았으니 그럼 traveler2도 한번 살펴보겠습니다.

<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FehNTWD%2Fbtq8PvEhMzl%2FmfcBIGR4BLa2k4WWyI0TNK%2Fimg.png">

<img src= "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc7JdgE%2Fbtq8OsncFik%2F3aRvKmKiwUMJ4BvRPcicdK%2Fimg.png">

traveler1과 다르게 retain이 가시적으로 추가된게 보이는데요 traveler1은 객체가 .init()으로 생성되었기 때문에 내부적으로 retain이 포함되어있다면 그와 다르게 traveler2는 traveler1에 대한 참조형으로 생성되기 때문에 명시적으로 retain을 해준것 같습니다.



이렇게 refrence counting을 retain 하고 release가 자동으로 관리되면서 이슈도 생기는데 

그 중 하나가 바로 유명한 순환참조입니다.



이 순환참조를 예방하기 위해서 보통 refrence count를 증가시키지 않는 weak, unowned를 사용하곤 하는데 무분별한 사용은 오히려 발견하기 어려운 내부 버그로 이어질 수 있다고 경고합니다! (이건 몰랐다...)



<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZwOUA%2Fbtq8JjMhMks%2FcTvK4Dijo4CfO0bhUHMH21%2Fimg.png">

Account는 traveler 를 weak으로 가지고 있기 때문에 refrence count를 증가 시키지 않습니다.

때문에 traveler 객체는 

```swift
traveler.account = account
```

를 마지막으로 release되면서 deallocate 되게 됩니다.

<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fk2xmM%2Fbtq8Ju0mItr%2FXhaUACCicdrCqoUob826P1%2Fimg.png"> 

사라져 버렸네용

이렇게 traveler는 메모리 해제가 되었는데 `account.printSummary()` 접근 하면 App Crash가 발생 할 수 있습니다.

왜냐하면 traveler는 옵셔널이니까여 ^__^ 

<img src= "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkRH8O%2Fbtq8NdYGjDH%2FBIjkJxq3fL6aXl8pNSJOo0%2Fimg.png">



>  그렇다면 옵셔널 바인딩으로 풀어주면 되는거 아님?

애플은 차라리 크래쉬가 더 좋다고 말한다.. 이러한 옵셔널 바인딩은 오히려 찾을 수 없는 버그를 만들 수 있다.

<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcBzJoJ%2Fbtq8OsAIOZf%2FAWIJ4e1JWtHsKYScfJfZek%2Fimg.png">

왜냐하면 traveler 객체가 deallocate 된 상태 에서 접근 하고 있을 수도 있고 traveler의 변경에 대해서도 예민해지게 되기 때문!



애플은 가능하면 weak, unowned를 순환참조 되지 않는 strong으로 리디자인하라고 추천한다.

> [withExtendedLifeTime()](https://developer.apple.com/documentation/swift/1541033-withextendedlifetime) 을 사용하는 방법도 있지만 추천하지 않는다기에 자세한 설명은 패스..



<img src= "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbXTvg9%2Fbtq8MGMKsk7%2FfyWFBk3WC9fie5PfNuAgT1%2Fimg.png">

이렇게 되면 순환참조와 weak, unowned 를 모두 방지 할 수 있다.



---

느낀 점...

순환 참조를 막기 위해 막현한 weak, unowned의 사용 남발은 오히려 slient bug 로 이어 질 수 있다는 것에 놀랐다..

그만큼 strong한 구조를 짜야 한다.. (설계단계에서 비용은 높겠지만 유지보수 비용이 훨씬 낮아진다.)





참고 사이트

- [https://cozzin.tistory.com/81](https://cozzin.tistory.com/81)

- [https://sujinnaljin.medium.com/ios-arc-%EB%BF%8C%EC%8B%9C%EA%B8%B0-9b3e5dc23814](https://sujinnaljin.medium.com/ios-arc-%EB%BF%8C%EC%8B%9C%EA%B8%B0-9b3e5dc23814)

