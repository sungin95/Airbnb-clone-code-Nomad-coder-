## 7.0

ORM은 장고 같은 경우 파이썬 언어를 통하여 데이터 베이스와 소통 할 수 있게 하는 것입니다. 



Room.objects

<django.db.models.manager.Manager object at 0x7f344c93b700

room.amenities

<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f344c93b910>

보면 그냥 objects는 Manager 에 의해 관리가 되는데. 관계를 통해 불러오는 경우 관리자가 바뀌게 된다. 



## 7.1

.objects는 Manager이라고 불린다. (데이터베이스와 소통할 수 있게 도와주는 인터페이스)

클래스에 최소 1개 이상 있음

모든 클래스에는 .objects가 있고 이름을 바꿀 수도 있음

 

filter는 정말 강력한 기능이다. 

Room.objects.filter(price__gt=15)

price 15이상 불러온다. 

Room.objects.filter(name__contains='서울')

name에 서울이 들어있는 모두

Room.objects.filter(name__startswith='Apt')

name이 Apt로 시작하는 모두



.create()

.delelte()



## 7.2 QuerySet

QuerySet이란 연산자를 함께 묶어주는 일을 한다. 

묶음 + QuerySet를 받게 되는데. 다시 필터링을 하려고 하면 QuerySet으로 묶여 있기 때문에 가능하다. 



Room.objects.filter(pet_friendly=True).exclude(price__lt=15).filter(name\_\_contains='서울')

Room.objects.filter(pet_friendly=True,name\_\_contains='서울').exclude(price__lt=15)

Room.objects.filter(pet_friendly=True,name\_\_contains='서울').count()

Room.objects.all()[:5]



QuerySet은 게으르다. 무슨 말이냐면 실제로 데이터를 가져오도록 요청받았을 때만 데이터베이스와 소통할 것이다. 

그러니까 내가 이름을 가져와 달라고 한 다음에 해당 데이터를 가져온다.



## 7.3

`__contains` 는 lookup이라고 불린다. 

`--exact`, `__iexact` 완전히 똑같은거. i는 대소문자 구분 없이

contains 는 SQL의 LIKE와 같다. 

Room.objects.filter(price__lt=15).exists()

True

```python
model
def total_amenities(self):
    return self.amenities.count()

admin
def total_amenities(self, room):
    return room.amenities.count()
```





## 7.4 Reverse Accessor 시작(set_)

`Room.objects.filter(owner__username='dlrkehrud')`

이런것도 되네ㄷㄷ

`Room.objects.filter(owner__username__startswith='no')`

 이렇게도 되지만 user를 통해 room을 알고 싶을 수 있다. 



## 7.5 Reverse Accessor

dir을 사용하면 모든 메서드, 속성등 다 알 수 있다. 

그리고 review_set, room_set등이 있다. 



ForeignKey를 통해 만들면 사용 할 수 있다. (manytomany도 될건데???)



## 7.6 related_name (_set 이름 바꾸어 주기)



















