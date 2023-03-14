from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1  # 관계가 있는 id의 정보도 보인다.


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
