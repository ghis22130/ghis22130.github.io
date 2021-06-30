---
layout: post
title: xcrun error 해결하기
comments: true
tags: [OS, DB, MySQL, Docker]
category: [SwiftBasics]
---

### 💢xcrun: error

터미널을 통해서 git을 자주 애용하던 중 갑자기 git 추적이 실패하기 시작했다!

<p align ="center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/xcrun.png?raw=true"></p>



```
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools),
missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```



이게 무슨일인가 뭐가 삭제되거나 경로가 꼬였나.. 나의 작업물들은 어떻게 되는 건가에 대한 두려움에 휩싸여 얼른 찾아보았다.



다행히 해결방법은 간단했다!

우선 원인은 Big Sur의 업데이트로 인해 Xcode 의존성 문제가 발생했다. (솔직히 무슨말인지 잘 모르겠다)



Xcode를 재설치 하면 해결 되지만 Xcode Comand Line Tools만 재설치 할 수 있는 명령어가 있다고 한다.



```
xcode-select --install
```

설치하겠냐는 문구와 함께 약 2분 정도만 기다리면 말끔히 해결된다 😃

찾아보니 업데이트할때 마다 발생하는 이슈같아서 계속 참고용으로 정리해보았습니다.

> 이 게시물은 어느 카테고리로 가야할지 모르겠다...