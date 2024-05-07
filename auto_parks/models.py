from django.db import models


class AutoParkModel(models.Model):

    name = models.CharField(max_length=25)

