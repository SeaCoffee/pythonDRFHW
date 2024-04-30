from django.db import models

class CarModel(models.Model):
    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats = models.IntegerField()
    carBody = models.CharField(max_length=25, default='sedan')
    engine = models.FloatField()
