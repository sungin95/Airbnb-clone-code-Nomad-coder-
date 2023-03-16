from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):
    # 재 정의 및 데이터 타입까지 변환 시킴
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    # 얘는 모든 데이터를 받는다. 에러 상황에서는 필드 없이 에러값을 띄운다.
    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError("체크인 날짜가 체크아웃 날짜보다 먼저 와야 합니다.")
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out_gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError("이미 예약이 돼있습니다. ")

        return data


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
