from django.db import models

class UsersModel(models.Model):

    name = models.CharField(max_length=25)