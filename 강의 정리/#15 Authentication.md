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

JSON Web Token은 데이터베이스에 공간을 전혀 차지하지 않는다. 

Auth Token은 공간을 차지한다. 



JWT는 암호화된 정보를 담고 있는 토큰을 유저에게 주고 (유저의 정보가 들어 있다. )

유저는 그 토큰을 가지고 있다가 다시 준다. 

토큰을 확인한다.

 

문제점. 유저를 강제로 로그아웃을 시킬 수가 없다. 



pyJWT라는 라이브러리 사용



JWT토큰은 우리가 준 토큰인지, 수정되었는지 아닌지를 알 수 있다. 





## 6 .env

django-environ을 들어간다. 

 `python -m pip install django-environ`

