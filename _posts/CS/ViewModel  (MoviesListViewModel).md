**ViewModel : (MoviesListViewModel)**

UseCase

Action



**UseCase**

Repository

func excute(requestValue, cached, completion)



**Repository**

DataTransferService

ResponseStorage

func fetchBanchanList(cached, completion)

- requestDTO
- cache
- endpoint = APIEndpoint -> Network



**DataTransferService**

NetworkService



**NetworkService**

func request( )