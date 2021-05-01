# Clean Architecture을 적용한 MVVM 패턴을 파해쳐보자! (진행중)



MVC 패턴을 적용하여 개발하다 보면 Model, View, Controller 셋 중에 어디에 넣어야 할 지 애매한(?) 상황이 꽤 자주 발생했는데요! 

사실 MVC 패턴도 완벽하게 이해하고 적용하고 있지 않기 때문에라는 생각이 들었지만 MVVM 패턴의 흐름도를 보고 꽤 흥미가 당겨 공부해보기로 했지만 

막상 적용해보려 하니 꽤나 복잡한 흐름이더군요... 🥲



그래서 [iOS-Clean-Architecture](https://github.com/kudoleh/iOS-Clean-Architecture-MVVM) 예제를 하나하나 뜯어가며 MVVM에 대해서 파악해보고자 합니다!

예제에 있는 계층도도 프로젝트에 맞게 이해하기 쉽게 되어있지만 막상 코드를 파해쳐 보면 어느새 숲 한가운데서 길을 잃고 있는 저를 발견하곤 했는데 천천히... 정말 아주 천천히.. 파해쳐 보겠습니다.

<p align ="center"><img src = "https://github.com/kudoleh/iOS-Clean-Architecture-MVVM/raw/master/README_FILES/CleanArchitecture+MVVM.png?raw=true " width = "80%"></p>

## Layer



<p align = "center">
  <img src = https://github.com/kudoleh/iOS-Clean-Architecture-MVVM/raw/master/README_FILES/CleanArchitectureDependencies.png?raw=true width = "80%"
</p>

위 이미지에는 Presentation, Domain, Data 크게 세가지 영역으로 표시했지만 부가적으로 앱의 셋팅과 흐름을 담당하는 `Application`, 네트워크와 관련된 객체들을 가지는 `Infrastructure` 가 존재합니다.



## Application Layer

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM01.png?raw=true"></p>

본격적으로 해부를 시작할 계층은 Application인데요!

앱 실행전 객체들의 의존성을 주입하고 셋팅 하는 계층입니다. 이 예제에서는 AppDelegate에서 했지만 저는 SceneDelegate로 옮겨서 적용했다. AppDelegate와 SceneDelegate의 차이점도 나중에 따로 정리를 한번 해야겠어요!



자... 어디보자.. AppDelegate는 알겠는데.. 나머지는 너무 생소하네요.. 우선 AppDlegate 부터 봅시다!



### AppDelegate

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM-AppDelegate01.png?raw=true"></p>



SceneDelegate라 생각하고 보렵니다!

이 델레게이트는 **AppDIContainer** 와 **AppFlowCoordinator**를 가지고 있네요. rootViewController가 될 UINavigationController를 선언해 준뒤 코디네이터에 네비게이션컨트롤러와 addDIContainer를 인자로 넘겨 객체를 생성해주네요!



그러고 .start로 앱을 실행하려나봐요 

음 그러니까 AppDelegate에서는 앱의 의존성(App Dependencies)을 정의하고 흐름을 담당하는 코디네이터에게 네비게이션컨트롤러와 AppDIContainer를 넘겨 다음 작업을 하게끔 넘겨주는 역할! 까지 하는것 같습니다



그러면 AppDIContainer는 과연 어떤 Dependencies를 정의하고 있는지 봅시다!



### AppDIContainer

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM-AppDIContainer.png?raw=true"></p>



이녀석이 AppDIContainer 이군요..! 

어디보자..

AppConfiguration이 존재하네요 이 녀석은 api의 key, baseURL과 같은 앱과 관련되어 정의되는 값들을 info.plist에 저장해 놓고 불러오는데 아직 저는 api를 사용하긴 하지만..? 이정도 까지 아니기에 패스.. 



Configuration을 정해준다음 네트워크도 config해주네요 저는 이러한 config에 대한 정보를 APIEndPoint 객체에 담아주기로 했기 때문에 넘어갑시다!



그다음 

```swift
func makeMoviesSceneDIContainer() -> MoviesSceneDIContainer { }
```

이 함수를 호출하여 `MoviesSceneDIContainer` 를 생성 및 반환 하네요.



**AppDIContainer** 의 역할은 앱의 관련된 기본적인 key, baseURL(s)를 불러오고 configure을 정의 해줌 -> network와 연동이 필요한 service들을 생성해줌 -> networkService들을 인자로 넘겨 SceneDIContainer를 생성 및 반환 하는 역할!



의 순서로 역할을 정의 해볼 수 있을 것 같습니다!



### MoviesSceneDIContainer

자자자 코드를 파해치다 보면 길을 잃기 너무 쉽기 때문에 저희가 지금 왜 여기 바로 MoviesSceneDIContainer에 와있는지 정리해봅시다!



**AppDelegate**에서 **AppFlowCoordinator**을 통해 앱을 움직이려 하는데 의존성 주입이 필요하게되죠!

그래서 **AppDIContainer**에서 앱관련 configure와 NetworkService 객체 생성 한 뒤 본격 적인 이 서비스들과 함께 Presentation, Domain, Data의 의존성 주입을 MoviesSceneDIContainer에서 하도록 부탁합니다!



그래서 이 녀석에서 많은 객체들이 유기적인 흐름으로 이루어 질 예정인거 같군요!



자 그럼 이제 한번 봐 봅시다.

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM-SceneDIContainer.png?raw=true"></p>



예제 코드로 봐보려 했으나...! 너무 많은 Scene에 대한 의존성 주입이 얽혀있어 설명하기엔 너무 장황해질거 같아 단일 Scene에 대해서 저의 예제코드(?)로 살펴 보려 합니당.



`BanchanSceneFlowCoordinatorDependencies`는 뭐하는 프로토콜이야? 는 나중에 다루도록 하구요.

외부에서 주입받은 networkService를 Repository에 주입해서 **Repository** 객체 생성

**Repository** 를 **UseCase** 에 주입하여 객체 생성

**UseCase** 들을 **ViewModel** 에 주입하여 객체생성 

아 이때 Repository나  UseCase들을 필요한 만큼 생성해서 넣어 줄 수 있어요 저는 다 단일 단계라 하나씩 넣었습니다.

마지막으로 **ViewModel** 을 가지고 있는 **ViewController** 를 생성하는 단계 까지가 의존성 주입이라 볼 수 있습니다!



흠.. 🧐 왜 이런짓을 하냐고요? 나중에 **TDD** 나 **SOLID** 에 대해 다룰 수 있음 좋겠지만 우선 해야합니다.. 우선



그런데 Flow Coordinator와 위에서 말한 프로토콜에 대해 말을 안했죠? 

이제 진짜 본격적으로 App이 아니라 Scene의 Flow를 정하러 가봅시다!



가기 전 다시한번  MoviesSceneDIContainer는 Presentaion, Data, Domain과 Network의 의존성 설정의 역할을 한다! 라고 정리해볼 수 있겠습니다.



### MoviesSearchFlowCoordinator

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM-MoviesSearchFlowCoordinator01.png?raw=true"></p>

와.. 아찔하네요.. 음 우리는 시작이 중요한거니까.. 시작에 관련된 것만 짤라서 봐봅시다!

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM-MoviesSearchFlowCoordinator02.png?raw=true"></p>

짠

음 우선 navigationController를 가지고 있고 음? 아까 봤던 MoviesSearchFlowCoordinatorDependencies가 여기 프로퍼티로 존재하네요?

저건 뭐하는거지

<p align = "center"><img src = "https://github.com/ghis22130/ghis22130.github.io/blob/main/assets/img/iOS_img/MVVM-MoviesSearchFlowCoordinator03.png?raw=true"></p>



