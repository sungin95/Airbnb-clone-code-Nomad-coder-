## 0

`poetry add djangorestframework`

settings 에서 rest_framework 를 추가해 주고

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS 

순서를 바꾸어 주자



## 1

카테고리는 모델도 하나이고 필드도 2개 밖에 없지만 따로 분리하여 앱을 만들 이유는

rooms와 experiences 2개의 앱에서 사용해야 되기 때문이다. 

GET POST /categories

GET PUT DELETE /categories/1

관리자/일반 사용자 구분



## 2

```python
from django.core import serializers
"categories": serializers.serialize("json", all_categories),
```

기존의 방법 지금은 사용하지 않음



REST Framework 를 사용할 것이고, 이것을 위해 데코레이터를 활용해야 한다. 



## 3

serializer를 통해 JSON으로 번역을 해 주어야 한다. 

.all()처럼 여러개를 주는 경우 many=True 욥션을 주어야 한다. 

그리고 serializer는 무엇을 번역할지, 어떻게 출력할 지를 결정할 수 있다. 



## 4

api_view()은 기본적으로 GET만 허용. POST도 허용 하고 싶다면 api_view(["GET","POST"])를 하면 된다. 

그러면 페이지에 get으로 보이는 페이지 하나, POST테스트 할 수 있는 페이지 하나가 생긴다. 

나중에는 설정에서 사용 안하도록 해야 한다. 



serializer는 번역을 하는 역할도 하지만 데이터를 검증하는 역할도 한다. 



## 5 is_valid()

검증 조건은 serializer을 통해 할 수 있다. 

read_only=True 를 통하여 데이터를 안 받아도 통과 가능



## 6

​    def create(self, validated_data):

```python
# Category.objects.create(
# name=validated_data["name"],
# kind=validated_data["kind"],
# )

# ** 딕셔너리를 가져온다. 알아서 매칭해 준다.
return Category.objects.create(**validated_data)
```



## 7 update

data = {'name':'nico'}

data.get('fav_food','pizza')

찾았는데 없으면 오른쪽 값을 호출한다. 



## 11 serializers.ModelSerializer

```python
class CategorrySerializer(serializers.ModelSerializer):
	class Meta:
        model = Category
        # 선택 혹은 제외
        # fields = ("__all__")
        exclude = ("created_at",)
```

id = IntegerField(label='ID', read_only=True)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
    name = CharField(max_length=50)
    kind = ChoiceField(choices=[('rooms', 'Rooms'), ('experiences', 'Experiences')])

위는 프린트를 한 값인데. 보면 created_at, updated_at은 read_only=True로 자동 세팅 한 것을 볼 수 있다. 



## ViewSet

views

```python
class CategoryViewSet(ModelViewSet):
    # 두가지를 알아야 한다. serializer와 object

    serializer_class = CategorrySerializer
    queryset = Category.objects.all()
```

urls

```python
from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",  # pk이름을 바꾸면 다시 설정해 줘야 한다.
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
```

끝

플러스 HTTP Form도 제공해 준다. 



## 13

반드시 viewset이 정답은 아니다. 왜냐하면 세세하게 컨트롤 하기 힘들고 오랜 시간이 지나 다시 봤을때 이해하기 어렵다. 그래서 앞으로는 APIView를 사용할 예정이다. 

