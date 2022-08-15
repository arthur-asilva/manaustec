from asyncio import proactor_events
from django.db import models
from apps.profiles.models import Profile

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=10, null=True)
    profile = models.ForeignKey(Profile, related_name="profile", on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=False)

    @classmethod
    def create(cls, request):
        user = cls(
            name = request['name'],
            email = request['email'],
            profile = Profile.objects.get(id=request['profile']),
            is_active = request['is_active']
        )
        user.save()
        return user
    
    @classmethod
    def update(cls, request):
        user = cls.objects.filter(id=request['id']).update(
            name = request['name'],
            email = request['email'],
            profile = Profile.objects.get(id=request['profile']),
            is_active = request['is_active']
        )
        return user

    def __str__(self):
        is_active = 'Ativo'
        if not self.is_active:
            is_active = 'Inativo'
        return f"{self.name}, {self.profile.name} ({is_active})."
