from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Perk, Experience
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializes import CategorrySerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceDetailSerializer(ModelSerializer):
    # owner의 특정 정보만 보내기 위해 설정, read_only를 통해 생성시 owner정보 요구X
    host = TinyUserSerializer(
        read_only=True,
    )
    category = CategorrySerializer(
        read_only=True,
    )
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Experience
        fields = "__all__"
        # exclude = ("perks",)

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user

    def get_is_liked(self, experience):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user=request.user,
            experiences__pk=experience.pk,
        ).exists()


class ExperienceListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Experience
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "address",
            "rating",
            "photos",
            "start_at",
            "end",
        )

    def get_rating(self, room):
        return room.rating()
