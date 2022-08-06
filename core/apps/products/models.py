from unicodedata import decimal, name
from django.db import models 
from apps.providers.models import Provider

class Product(models.Model):
    name = models.CharField(max_length=254)
    purchase_price = models.FloatField()
    sale_price = models.FloatField()
    quantity = models.IntegerField(null=True, blank=True)
    provider = models.ForeignKey(Provider, related_name="provider", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.quantity}"

    @property
    def sale_price(self):
         return self.sale_price

    @sale_price.setter
    def sale_price(self, value):
         self.sale_price = float("{:.2f}".format(value))