from rest_framework import serializers
# pip install Django django-rest-framework
from .models import USerVo as user

class UserSerializer(serializers.Serializer):
    username : serializers.CharField()
    password : serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    birth = serializers.CharField()
    address = serializers.CharField()
    class Meta:
        model = user
        fields = '__all__'

    def create(self, valided_data):
        return user.objects.create(**valided_data)

    def update(self, instance, validated_data):
        user.objects.filter(pk=instance.username).update(**validated_data)