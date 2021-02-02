---
layout: post
title: Network FrameWork를 이용한 HTTP 통신
comments: true
tags: [OS, DB, MySQL, Docker]
category: [SwiftBasics]
---

HTTP 요청 실습을 하기 위해서 Swift Framework 중 하나인 Network를 사용해야 했는데 이에 대한 한글뿐 아니라 정리 문서가 너무 빈약해서 애 먹었다... 

꽤나 최신에 나온 프레임워크인거 같기도 하고 사용용도가 기기의 인터넷 연결 유무(Monitor)에 대한 예제만 가득가득했다.



완벽한 정의라 할 수 절대 없지만 내가 느낀데로 정리해보려 한다.



## NWEndpoint

<p align = "center"><img src ="https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/NWF01.png?raw=true" width = "70%"></p>

네트워크 연결의 로컬 또는 원격 Endpoint. 즉 통신하고자 하는 종단을 말하고자 하는것 같다.

<p align = "center"><img src ="https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/NWF02.png?raw=true" width = "70%"></p>



NWEndpoint는 enum형태의 Host와 struct형태의 Port를 가지는데 생성과 동시에 초기화도 가능하고 각각 따로 관리하고자 하면 따로도 생성해줄 수 있다.



## NWParameters

통신을 어떠한 방식으로 할것인가를 정의해준다. 

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/NWF03.png?raw=true"></p>


## NWConnection

> A bidirectional data connection between a local endpoint and a remote endpoint.
>
> 로컬 끝점과 원격 끝점 사이의 양방향 데이터 연결입니다.



나는 www.disney.com에 HTTP 규약을 지킨 Request Header를 전송하고자 했다.

흐름을 살펴보면 NWEndpoint로 원격 endpoint를 disney로 설정해주고 NWParameter로 통신 방법 ( 나는 tcp로 하고자 한다.) 을 설정해준 뒤에 NWConnection으로 데이터가 오고 갈수 있도록 연결 해주는것으로 이해할 수 있겠다.



```swift
import Network

class Requester {
  private var host: NWEndpoint.Host
  private var port: NWEndpoint.Port
  private var parameter: NWParameters
  
  init(host: NWEndpoint.Host, port: NWEndpoint.Port, parameter: NWParameters) {
    self.host = host
    self.port = port
    self.parameter = parameter
  }
  
  func createConnection() {
    let connection = NWConnection(host: host, port: port, using: parameter)
  }
}
```



Connection 까지의 생성 예제이다. Network 통신은 **비동기**로 이루어져야 한다. 때문에 연결을 실행시켜주기 위해서는 실행 큐를 입력해줘야하는데 나는 `DispatchQueue.global()` 로 해주었다.



Connection 객체가 생성이 되면 이 Conecction의 상태를 다뤄줄 핸들러 `stateUpdateHandler`가 존재한다. Conecction의 state는 다양하게 존재하지만 우선 ready상태가 되어야 Conecction이 성공적으로 이루어졌고 통신할 준비가 되었다 할 수 있다.

```swift
func createConnection() {
        let connection = NWConnection(host: host, port: port, using: parameter)
        connection.stateUpdateHandler = { state in
            switch state {
            case .ready:
                print("🙌 Connection is success!")
                self.sendMessage(connection)
            case .waiting(let error):
                print("Connection is waiting")
                print(error)
            case .failed(let error):
                print("Connection is failed")
                print(error)
            default:
                print("Connection is \(connection.state)")
                break
            }
        }
        connection.start(queue: DispatchQueue.global())
}
```



## send와 receive

자 이제 통신을 위해 연결은 완료되었다. Conecction이 ready상태가 되었을 때! 이제야 비로소 disney.com에 HTTP 규약에 맞게끔 헤더를 작성한뒤 send하면 그게 알맞는 규약으로 Response가 올것을 기대한다...**(되야한다...)**



우선 HTTP Request Header의 구조를 살펴봐야 했다.

크롬의 개발자모드를 실행한 뒤 http://www.disney.com 입력하고 엔터를 팍 떼리면 실제로 어떤식으로 응답이 오고가고 있는지 확인 해볼 수 있다!


<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/NWF05.png?raw=true"></p>




오호 저 규약을 지키면 서버 쪽에서 Response를 주겠구나

근데 저건 너무 긴데?  최소한의 정보만 넘겨주고싶다..



#### NWConnection.send(data: , completion:)

이 부분에서 가장 애를 많이 먹었다. 

```swift
let data = """
    GET /home/index.jsp HTTP/1.1
    Host: www.disney.co.kr
    Accept-Language: en-US,en;q=0.9,ko;q=0.8
"""
```

헤더를 이렇게 작성해서 무작정 send하고 있었기 때문이다.



한번 헤더를 조금 더 자세하게 살펴보기로 했다.

개밸자 모드에서 본 것은 편의를 위해 `\r\n`이 삽입 되어있었던것이다. 데이터 가공을 하기 위해 data를 건드려주기로 했다.

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/NWF04.png?raw=true" width = "80%></p>

*출처 : JK*

오호.. \n을 \r\n으로 대채해주자 그리고 헤더의 끝을 알리기 위해 개행해주자!

```swift
let data = data.appending("\n\n".replacingOccurrences(of: "\n", with: "\r\n")).data(using: .utf8)
```

짜잔 가공이 완료되었다.



#### NWConnection.SendCompletion

이때 쯤 등장해줘야 하는 또 다른 난관 

completion이 뭘까..?

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/Swift_img/NWF06.png?raw=true"></p>

contentProcessed 는 보낸 데이터가 스택에 의해 처리될 때 호출되는 완료 핸들러를 제공한다.

idempotent는 데이터를 여러번 보낼 수 있는 멱등의 데이터를 표시한다..?

솔직히 이건 잘 모르겠다. 찾아보니 다들 contentProcessed를 사용한뒤 Error를 다뤄주길래 나도 이걸로 했다.

> 나중에 모두 구현완성하고 둘 다 돌려 보았는데 차이를 느끼지 못했다...🙍‍♂️



자 이제 우리는 www.disney.com에 당당하게 Request 할 준비가 되었다!

```swift
func sendMessage(_ connection: NWConnection) {
  let data = header.appending("\n\n").replacingOccurrences(of: "\n", with: "\r\n").data(using: .utf8)
  let completion = NWConnection.SencCompletion.contentProcessed { (error: NWError?) in print(error)}  // Need error handlig 
  connection.send(content: data, completion: completion)
  self.receiveMessage(connection)
}
```

이렇게 보내주고 나면 통신이 제대로 이루어졌는지 알 수 있는 방법이 직관적으로는 없다..ㅎ

이걸 확인하기 위해서는 Wireshark로 HTTP 통신을 추적하는 방법이 있다.

<p align = "center"><img src = "https://github.com/ghis22130/CODESQUAD_Masters_iOS/blob/main/images/CS10-Day09/network1.png?raw=true"></p>

보인다 보여! GET /home/index.jsp HTTP/1.1 나의 Request에  `HTTp/1.1 200 200`  으로 나의 요구를 잘 받았음을 확인 시켜주는 디즈니! 자 이제 디즈니의 답변을 읽어봐야한다.

```swift
func receiveMessage(_ connection: NWConnection){
  print("Receiving Data...")
  connection.receiveMessage(completion : {data, context, bool, error} in
     if let data = data{
       print("\n\n", String(data: data, encoding: .utf8)??"Empty")
     } else { print("Error:", error)} 
     if !bool {
       self.receiveMessage(connection)
     }
   })
}
```

 Response data를 받는 방법에는 두가지가 있는것 같다.

`receiveMessage` 혹은 `receive` 나는 receiveMessage를 사용하였는데 둘의 차이점 또한 한번 알아봐야겠다



여하튼 이렇게 요청을 비동기로 실행하고 조금의 기다림 끝에 디즈니의 답변을 출력해볼 수 있다.

#### Response Header

<p align = "center"><img src = "https://github.com/ghis22130/CODESQUAD_Masters_iOS/blob/main/images/CS10-Day09/network3.png?raw=true"></p>

#### Response Body

<p align = "center"><img src = "https://github.com/ghis22130/CODESQUAD_Masters_iOS/blob/main/images/CS10-Day09/network4.png?raw=true"></p>

영롱하다 영롱해..



## 마치며

제가 작성한 스크립트에는 분명히 오류와 역설(?)이 존재함을 인지하고 있습니다..!

나중에 또 한번 이 프레임워크를 사용할 날이 올 때면  다시 힘든 방대한 구글링을 조금이라도 줄이고자 작성 해보았습니다.

