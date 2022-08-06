from django.db import models
from apps.profiles.models import Profile

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=10)
    profile = models.ForeignKey(Profile, related_name="profile", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        is_active = 'Ativo'
        if not self.is_active:
            is_active = 'Inativo'
        return f"{self.name}, {self.profile.name} ({is_active})."
