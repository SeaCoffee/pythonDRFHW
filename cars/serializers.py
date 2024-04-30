from rest_framework import serializers
from cars.models import CarModel

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=25)
    seats = serializers.IntegerField()
    year = serializers.IntegerField()
    carBody = serializers.CharField(max_length=25)
    engine = serializers.FloatField()

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class CarListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=25)
    year = serializers.IntegerField()