## 3

인증 방법은 총 4가지가 있다. 

그중 베이직 방법은 아무도 안쓰고

토큰 방식이 있는데. 장고에서 제공해 준다. 

THIRD_PARTY_APPS 에 추가

`rest_framework.authtoken`

그리고 `migrate`

그리고 

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",  # 기본 값
        .......
        "rest_framework.authentication.TokenAuthentication", # 추가
    ]
}
```

어드민 페이지에 가면 인증토큰이 추가 된걸 확인 할 수 있다. 





이제 users.urls에 추가

```python 
from rest_framework.authtoken.views import obtain_auth_token
path("token-login", obtain_auth_token),
```

해당 페이지에 username과 password를 보내면 토큰 번호가 온다. 

이 토큰 번호를 헤더에 

`Authorization`

`Token 토큰번호`

이렇게 넣으면 인증이 된걸 확인 할 수 있다. 



만약 카카오톡 로그인 처럼 다른 방식의 토큰이 필요하면 `obtain_auth_token`이 방식을 사용 안해도 된다. 



정리 토큰 번호를 보내면 

`"rest_framework.authentication.TokenAuthentication"` 여기에서 user가 누구인지 찾게 되고 

인증이 된다. 



## 4 JWT

