from django.db import models
from core.models import BaseModel

from auto_parks.models import AutoParkModel


class CarModel(BaseModel):

    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    body_type = models.CharField(max_length=50, default='Sedan')
    engine = models.FloatField()
    auto_parks = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars', default=1)