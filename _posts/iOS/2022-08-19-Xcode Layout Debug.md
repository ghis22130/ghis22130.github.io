---
layout: post
title: URLSession에 대해 알아보자!
comments: true
tags: [iOS,XCode]
category: [iOS]
---

### URLSession이란?

iOS에서 서버와 HTTP 프로토콜로 데이터 통신을 하기 위해 애플에서 재공하는 API



### URLSession 사용순서

- Configuration 을 결정 
  - default, ephemeral, background 케이스를 가질 수 있다.
    - Default : 기본 통신으로 디스크 기반 캐싱을 지원합니다.
    - Ephemeral : 쿠키나 캐시를 저장하지 않는 정책을 가져갈 때 사용합니다. (ex. Safari의 개인정보보호 모드)
    - Background : 앱이 백그라운드에 있는 상황에서 컨텐츠 다운로드, 업로드를 할 때 사용합니다.
    - 앱이 종료돼도 통신이 이뤄지는 것을 지원하는 세션

- Session  생성
- URLRequest 에 사용할 url 결정 (with param..)

- Task 종류 결정

  - DataTask

    - Data를 받는 작업, Response 데이터를 메모리 상에서 처리하게 됩니다.
    - 백그라운드 세션에 대한 지원이 되지 않습니다.
    - URL 요청을 실시하고 완료 시 핸들러를 호출하는 Task 형식
    - Task가 실행된 후 핸들러가 실행되기 때문에 탈출 Closure 형태로 받아와야 합니다.

    UploadTask

    - 파일을 업로드할 때 사용합니다.

    DownloadTask

    - 파일을 다운로드 받아서 디스크에 쓸 때 사용합니다.





참고 사이트

[https://greatpapa.tistory.com/66](https://greatpapa.tistory.com/66)

[https://kor45cw.tistory.com/295](https://kor45cw.tistory.com/295)  <- 예제 코드 감동적이다..

