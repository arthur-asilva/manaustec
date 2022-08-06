from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
