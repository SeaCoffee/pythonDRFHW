from rest_framework import serializers
from cars.models import CarModel

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'engine', 'created_at', 'updated_at')


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year')