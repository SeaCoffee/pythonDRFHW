from rest_framework import serializers

from auto_parks.models import AutoParkModel
from cars.serializers import CarSerializer

class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')