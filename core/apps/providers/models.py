from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    address = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.name}"
