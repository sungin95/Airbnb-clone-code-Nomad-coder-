from rest_framework import serializers
from .models import Category


class CategorrySerializer(serializers.ModelSerializer):  # Serializer->ModelSerializer
    # 이렇게 설정해 주면 아래 작업을 대 해 준다.
    class Meta:
        model = Category
        # 선택 혹은 제외
        fields = "__all__"
        # fields = (
        #     "name",
        #     "kind",
        # )
        # exclude = ("created_at",)
        # create, update는 나중에 커스텀 할때 사용 기본적으로 있음

    # pk = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(
    #     required=True,
    #     max_length=50,  # is_valid때 활용
    # )
    # kind = serializers.ChoiceField(
    #     choices=Category.CategoryKindChoices.choices,
    # )
    # created_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     # Category.objects.create(
    #     #     name=validated_data["name"],
    #     #     kind=validated_data["kind"],
    #     # )
    #     # ** 딕셔너리를 가져온다. 알아서 매칭해 준다.
    #     return Category.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # 값 있으면 바꾸고 없으면 그대로
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.kind = validated_data.get("kind", instance.kind)
    #     instance.save()
    #     return instance
