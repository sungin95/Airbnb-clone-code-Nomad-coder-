# 0

`poetry add django-cors-headers`

특정 도메인이 fetch를 허용한다. (프론트서버와 백엔드 서버 연결을 위해 사용)



# 2

TanStack Query 사용

이걸 사용하면 편하게 fetch를 할 수 있다. 

`npm i @tanstack/react-query`

 리액트 QueryClientProvider, QueryClient 를 사용하면 캐싱을 해 줄 것이다. 

캐싱이 뭐지???

캐싱의 뜻은

만일 내가 404페이지로 간다가 오면 로딩을 하게 되는데. 이는 매번 화면에 들어올 때마다 fetch를 또 해 줘야 하기 때문이다. 

그런데 캐싱을 해 주게 되면 이를 기억하고 있어서 다시 fetch를 할 필요가 없다. 



# 3

`npm i axios`

axios는 fetch의 상위 호환이다. 

.json을 해 줄 필요가 없다. 



