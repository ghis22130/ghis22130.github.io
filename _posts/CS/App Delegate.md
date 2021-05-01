# App Delegate



# Scene Delegate

window scene 을 관리한다

ipad나 macOS는 scene 을 여러개 만들 수 있다 (  iOS 말고 ) -> 화면 분할 하기 위해서

iOS는 single window 최근에는 multi window 도 가능해지고 있다.



# View Controllers Container

**Tab Bar Container**

window 다음 route view controller에 위치해서 각각의 view controller를 관리함





여러개 VC로 addSubView하면 AutoLayout 유지하기가 힘들다.



**Navigation Controller**

navigation bar 을 보여주고 VC를 쌓아주기만 한다.



Container 끼리도 계층 구조가 형성될 수 있다.



**Split View Controller**

