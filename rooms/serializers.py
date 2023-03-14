from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializes import CategorrySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    # owner의 특정 정보만 보내기 위해 설정, read_only를 통해 생성시 owner정보 요구X
    owner = TinyUserSerializer(
        read_only=True,
    )
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )
    category = CategorrySerializer(
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )
        # depth = 1  # 관계가 있는 id의 정보도 보인다.
