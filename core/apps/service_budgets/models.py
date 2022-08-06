from http import client
from django.db import models
from apps.clients.models import Client
from django.contrib.postgres.fields import ArrayField
from apps.users.models import User

class ServiceBudgets(models.Model):
    client = models.ForeignKey(Client, related_name="client", on_delete=models.PROTECT)
    delivery_date = models.DateField()
    withdrawal_date = models.DateField()
    delivery_team = ArrayField(models.IntegerField())
    withdrawal_team = ArrayField(models.IntegerField())