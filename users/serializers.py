from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            #
            "gender",
            "language",
            "curreny",
        )


class PublicUserSerializer(ModelSerializer):
    roomsCount = SerializerMethodField()
    reviewsCount = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "avatar",
            "name",
            "gender",
            "username",
            "roomsCount",
            "reviewsCount",
        )

    def get_roomsCount(self, user):
        return user.rooms.count()

    def get_reviewsCount(self, user):
        return user.reviews.count()
