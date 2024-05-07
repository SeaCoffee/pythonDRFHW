from rest_framework import serializers

from users.models import UsersModel
from auto_parks.Serializer import AutoParkSerializer


class UsersSerializer(serializers.ModelSerializer):
    autoparks = AutoParkSerializer(many=True, read_only=True)

    class Meta:
        model = UsersModel
        fields = ('id', 'name', 'autoparks')