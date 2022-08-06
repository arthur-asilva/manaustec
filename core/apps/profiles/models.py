from operator import mod
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    modules = ArrayField(models.CharField(max_length=100))
    allowed_areas = ArrayField(ArrayField(models.CharField(max_length=100)))