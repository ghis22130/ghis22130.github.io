---
layout: post
title: Combine 시작하기(4)-Scheduler
comments: true
tags: [Swift,Apple,Guideline, Combine]
category: [SwiftBasics]
---  

이번 포스트에서는 Scheduler에 대해서 알아보고 Scheduler를 사용하는 방법에 대해서 알아보겠습니다.

* Scheduler는 무엇인가?  
    [Scheduler](https://developer.apple.com/documentation/combine/scheduler)는 언제(시간), 어떻게(스레드) Publisher의 작업들이 수행될지를 결정하기 위한 객체입니다. 비동기 처리에 있어서 시간과 스레드 전환 등의 옵션은 필수적으로 들어가야 하는데, 시간 혹은 스레드 관련 Operator는 이 Scheduler를 인자로 요구하기 때문에 반드시 알아야 하는 객체이기도 합니다. 

* Scheduler 사용하기  
    Scheduler는 직접 구현하는 것은 여러모로 복잡하기 때문에 직접 구현하는 것보다, 있는 것을 사용하는 게 좋습니다. Apple이 제공하는 Scheduler타입 객체는 DispatchQueue, OperationQueue, RunLoop등으로, 이미 이전부터 시간과 스레드 전환을 위해 사용하던 객체들입니다. 즉, 기존에 사용하던 객체를 그대로 Combine에서도 사용할 수 있습니다. 기존에 DispatchQueue를 사용할 때는 Closure를 직접 인자로 넘겨야 해서 중첩된 형태로 쓰다보니 여러번 스레드 전환을 하게되면 가독성이 떨어질 수 밖에 없었던 것을 Combine의 합성 형태로 바꿔주면서 좀 더 가독성을 높일 수 있다는 소소한 장점도 있습니다.

    ```swift
    [1,2,3,4,5,6,7,8,9,10].publisher
        .subscribe(on:DispatchQueue.main) // 전체 Publisher의 기본 동작을 메인 스레드에서 진행한다.(메인 스레드에서 동작)
        .delay(for: 2, scheduler: DispatchQueue.global()) // 백그라운드에서 2초간 delay를 준다. 이때 스레드도 바뀐다.(백그라운드 스레드에서 동작)
        .map({"\($0)"}) // Int를 String으로 바꿔준다.(백그라운드 스레드에서 동작)
        .receive(on: DispatchQueue.main) // 이후 동작은 메인 스레드에서 진행한다.
        .sink(receiveValue: { s in 
            self.label.text = s // 값을 받아서, label에 세팅한다(메인 스레드에서 동작)
        }).store(in: &self.cancelBag)
    ```  

    이외에 강제로 동기적으로 수행하도록 만드는 [ImmediateScheduler](https://developer.apple.com/documentation/combine/immediatescheduler)가 있습니다. 해당 스케쥴러에는 시간 옵션을 주어도 이를 무시하고 즉시 실행하는 특징을 가지고 있습니다.

Scheduler를 사용해서 비동기 처리를 적절한 스레드에서, 적절한 타이밍에서 동작하도록 조절하면 좀 더 효과적인 로직을 작성할 수 있게 됩니다.

---  

> 참고 자료
> [Documentation - Scheduelr](https://developer.apple.com/documentation/combine/scheduler)