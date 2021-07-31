---
layout: post
title: for Loop Labeling
comments: true
tags: [OS, DB, MySQL, Docker]
category: [SwiftBasics]
---

Swift에서 중첩 반복문 사용시 하위 반복문에서 조건 달성 하거나 이벤트 발생 시 하위 반복문 뿐만 아니라 상위 반복문까지 `break` 하거나 `continue`하는 방법이 항상 궁금해왔는데...



여지껏 제대로 알아보지 않은채 하위 반복문을 따로 함수로 모듈화 시켜 리턴값을 이용한 상위 반복문을 컨트롤 하는 방식으로 다뤄왔었음.. 귀찮았다.. ( 하지만 보기는 좋은듯.. 근데 알고리즘 문제 풀 때 일일히 함수로 빼고 있자고 하니 로직도 한눈에 안들어 오는거 같고 어케 하는거지.. ) 



그런데 for 반복문에 labeling 이 가능한 신세계를 발견하였다.

사용 방법은 아주 간단하였다! for 앞에 반복문의 이름으로 사용하고자 하는 라벨명을 `~~~: for _ in (1...10)` 과 같이 써주면 됐다!



백문이 불여일견이라 코드로 직접 봅시다

```swift
var x: [Int] = [1,2,3]
var y: [Int] = [4,5,6]

outerLoop: for i in y {
    innerLoop: for j in x {
        if j == 2 { continue outerLoop }
        print(i, j)
    }
}
```

이 얼마나 아름답나..

innerLoop가 안에서 사용되지 않으니까 구지 라벨링을 하지 않고 싶으면 하지 않아도 된다! 라벨링을 사용하려면 모든 for 문에 라벨링을 해야하는 조건이 없다는 뜻!



위 코드는 x가 2를 탐색하면 y가 continue 되는 형식!

물론 `continue` 와 동일하게 `break`ㅇ에도 적용이 가능합니다!!!!!



for문이 3개가 넘어간다구요? 걱정 ㄴㄴ

```swift
iLoop: for i in (0..<100) {
    jLoop: for j in (i+1)..<100 {
        if j == 5 { continue iLoop }
        kLoop: for k in (j+1)..<100 {
            if k == 99 { break jLoop }
        }
    }
}
```

뾰롱 이렇게도 가능하네요.. 좋은 예시인지는 모르겠지만 모든걸 녹였다 생각함..



이로써 중첩 반복문을 내가 원할 때 언제든 탈.출.할.수.있.다.!



이걸 이제 왜 발견했지 너무 당연해서 정보가 없었나.. 개꿀

오늘도 하나 배워갑니당 안뇽


참고사이트

[https://zeunny.tistory.com/26](https://zeunny.tistory.com/26)