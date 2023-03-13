## 0

`poetry add djangorestframework`

settings 에서 rest_framework 를 추가해 주고

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS 

순서를 바꾸어 주자



## 1

카테고리는 모델도 하나이고 필드도 2개 밖에 없지만 따로 분리하여 앱을 만들 이유는

rooms와 experiences 2개의 앱에서 사용해야 되기 때문이다. 

