from rest_framework import serializers


class CategorrySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
