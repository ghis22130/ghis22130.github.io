---
layout: post
title: 앱의 콘텐츠나 데이터 자체를 저장/보관하는 특별한 객체
comments: true
tags: [iOS,XCode]
category: [iOS]
---

## 💿 Core Data

**Core Data는 DataBase가 아님** ( Core Data는 ORM 매핑 프레임워크가 맞는 의미, 데이터 저장에 관한 일종의 프레임워크 )

**Core Data** 는 오프라인, 백그라운드 작업을 위해 사용하게된다.

- 애플리케이션의 영구 데이터 저장 ( 오프라인 )

- 임시 데이터를 캐싱

- 단일 기기에서 앱의 실행 취소 기능을 추가하는 프레임워크



### **Persistence**

Core Data는 개체를 저장소에 매핑하는 세부 정보를 추상화하여 데이터베이스를 직접 관리하지 않고도 Swift 및 Objective-C의 데이터를 쉽게 저장할 수 있습니다.

![https://docs-assets.developer.apple.com/published/5770f06627/73cb5bb3-06ab-4017-89da-84ddacd20279.png](https://docs-assets.developer.apple.com/published/5770f06627/73cb5bb3-06ab-4017-89da-84ddacd20279.png)

### **개별 또는 일괄 변경 사항 실행 취소 및 다시 실행**

Core Data의 실행 취소 관리자는 변경 사항을 추적하고 개별적으로, 그룹으로 또는 한 번에 모두 롤백 할 수 있으므로 앱에 실행 취소 및 다시 실행 지원을 쉽게 추가 할 수 있습니다.

![https://docs-assets.developer.apple.com/published/843104c2e8/8ff27b5a-9441-4054-91ec-152843782ce2.png](https://docs-assets.developer.apple.com/published/843104c2e8/8ff27b5a-9441-4054-91ec-152843782ce2.png)

### **백그라운드 데이터 작업**

백그라운드에서 JSON을 객체로 구문 분석하는 것과 같이 잠재적으로 UI 차단 데이터 작업을 수행합니다. 그런 다음 결과를 캐시하거나 저장하여 서버 왕복을 줄일 수 있습니다.

![https://docs-assets.developer.apple.com/published/1b9da4c41b/efc8be3c-1e32-4579-9356-4e029b99268a.png](https://docs-assets.developer.apple.com/published/1b9da4c41b/efc8be3c-1e32-4579-9356-4e029b99268a.png)

동기화보기, 버전관리 및 마이그레이션

`CoreData`는 데이터베이스의 테이블의 수가 적거나 테이블 간의 관계가 복잡하지 않다면 사용하지 않는 것이 좋다고함



<p aling = "center"><img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbwsdjQ%2FbtqC8HPrKsD%2FQ8WS51Q4svEaMy9YqznCVK%2Fimg.png"></p>



**1) 관리 객체(Managed Obejct) : NSManagedObject**

 table에서 레코드를 읽을 때 core data에서는 객체가 생성되는데, 이 객체를 저장하는 자료형

예) 직원들의 데이터를 다룰 때 DB에서 직원들의 정보를 읽어오면 이것을 그대로 사용하지 않고 VO인스턴스에 담아 사용, 이때 **VO가 관리 객체에 해당**

 

**2) 관리 객체 컨텍스트(Managed Object Context)**

 핵심적인 두 가지 역할

 (1) MO를 가지고 CRUD역할 (Core Data에서 생성되는 모든 관리 객체는 컨텍스트에 담겨 관리)

  \- 컨텍스트에 담긴 객체는 영구 저장소로 보내 저장, 삭제 가능

  \- core data는 메모리에 로드된 상태로 처리되는데, 이 때의 메모리가 "컨텍스트"를 의미

 (2) "영구 저장소"와 "영구 저장소 코디네이터"에 대한 관리자 역할

  \- 읽기와 쓰기를 영구 저장소에 요청 (DAO패턴과 유사)

 

**3) 영구 저장소 코디네이터(Persistent Store Coordinator)**

 컨텍스트와 직접 데이터를 주고 받으면서 다양한 영구 저장소들의 접근을 조정하고 입출력을 담당

 흐름 : 컨텍스트가 데이터 요청 -> 코디네이터가 요청을 받고, 영구 저장소에서 데이터 탐색 -> 코디 네이터가 MO인스턴스 생성하여 반환

 

**4) 관리 객체 모델(Managed Obejct Model)**

엔터티(Entity)의 구조를 정의하는 객체인 동시에 이를 바탕으로 MO패턴의 모델 클래스를 참조

※ MO vs MOM(Managed Object Model)

 \- MOM : 클래스이자 형식이고 구조를 의미

​        데이터를 CRUD하지 않으며 관리 객체의 각 요소를 제대로 담을 수 있도록 저장 데이터를 구조화

 \- MO : MOM을 바탕으로 생성된 인스턴스

 

**5) 영구 객체 저장소(Persistent Obejct Store)**

 **- 초기에는 직접 읽을 수 있으며 디버깅에 용이한 XML저장소 타입을 사용하며,**

  **앱을 배포할 당시 대량의 데이터를 고려하여 SQLite데이터베이스를 사용하는 것이 용이**

| 타입                                          | 설명                                                         |
| --------------------------------------------- | ------------------------------------------------------------ |
| 인메모리 저장소 타입 (NSInmemoryStoreType)    | 메모리 기반의 저장 방식(영구 저장소를 사용하지 않는 것) 앱 종료시 데이터 보존이 되지 않음 |
| 플랫 바이너리 저장소 타입 (NSBinaryStoreType) | 데이터를 단순 바이너리 파일 형식으로 저장 장점은 조회 성능 개선, 단점은 초기 로딩 시간 증가 |
| XML 저장소 타입 (NSXMLStoreType)              | 원자성 장점은 직접 열어보고 확인 가능(초기 디버깅용이), 단점은 처리 속도가 느림 |
| SQLite 데이터베이스 (NSSQLiteStoreType)       | 객체 그래프 중 일부만 로딩 가장 많이 사용                    |

\* 바이너리 방식은 원자성을 갖지만 SQLite같은 경우는 그렇지 않음(파일 손상이 발생할 가능성 존재)

 

※ "영구저장소"와 "레코드(메모리에 저장된 데이터)"사이의 데이터 교환 원리

 "차등저장(Differencial Save)매커니즘" : 매번 데이터 전체를 커밋하는 대신 마지막 저장 이후에 변경된 부분만 커밋, **save()메소드 호출**

 매 작업 단위마다 커밋을 하게 되면 오버헤드가 발생하므로 최대한 늦게 해주는 것이 효율적



### 코어 데이터의 한계

---

**1) in-memory방식 : 메모리에 로딩된 객체에 대해서만 수정 가능(SQLite는 메모리에 객체 모두를 로딩하지 않아도, 최소한의 데이터만 로드)**

in-memory에서 데이터 삭제시, 영구저장소에서 데이터 read -> 객체로 생성 -> 이것을 메모리에 로딩 -> 이를 삭제하고 다시 컨텍스트를 저장소에 커밋

 

**2) 데이터 로직에서의 한계**

 \- 중복된 값의 입력을 방지하는 "Unique"키가 없으므로, 애플리케이션에서 비즈니스 로직을 통해 처리해야 가능

 

**3) thread-safe하지 않음(싱글스레드 환경)**

thread끼리 Lock기능(다른 쓰레드가 침범하지 못하는 것)이 존재하지 않음(단 락을 걸지 않음으로써 빠르게 데이터 처리가 가능)

 \* SQLite역시 싱글 스레드만 지원



# 📝 User Defaults

앱 시작시 키-값 쌍을 지속적으로 저장하는 사용자의 기본 데이터베이스에 대한 인터페이스

앱의 기본 환경 설정과 같이 가벼운 정보를 저장한다.

1. 기본 개체 저장
2. 파일 참조 유지
3. 기본값 변경에 대한 대응
4. 관리되는 환경에서 기본값 사용

[구현 코드 참고](https://lemon-dev.tistory.com/entry/NSUserDefaults)


---
## 참고
[https://ios-development.tistory.com/89](https://ios-development.tistory.com/89)

[https://lemon-dev.tistory.com/entry/NSUserDefaults](https://lemon-dev.tistory.com/entry/NSUserDefaults)

[https://www.notion.so/bb8ebcc15a9342ff8fc0fd1555e13f14](https://www.notion.so/bb8ebcc15a9342ff8fc0fd1555e13f14)