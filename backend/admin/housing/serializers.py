from rest_framework import serializers
from admin.housing.models import Housing


class HousingSerializer(serializers.Serializer):
    housing_id = serializers.AutoField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    housing_median_age = serializers.FloatField()
    total_rooms = serializers.FloatField()
    total_bedrooms = serializers.FloatField()
    population = serializers.FloatField()
    households = serializers.FloatField()
    median_income = serializers.FloatField()
    median_house_value = serializers.FloatField()
    ocean_proximity = serializers.TextField()

    class Meta:
        model = Housing
        fileds = '__all__'

    def create(self, validated_data):
        return Housing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Housing.objects.filter(pk=instance.id).update(**validated_data)