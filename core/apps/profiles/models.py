from os import access
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    accesses = models.JSONField(default='{}')

    def __str__(self):
        return self.name 

    @classmethod
    def create(cls, request):
        access_list = Access.objects.values('access').filter(id__in=request.getlist('user_access')).values_list('access', flat=True)

        profile = cls(name = request['name'], accesses = list(access_list))
        profile.save()

        return profile

    @classmethod
    def update(cls, id, request):
        users_access = Access.objects.values('access').filter(id__in=request.getlist('user_access')).values_list('access', flat=True)

        access_list = {
            'users': list(users_access)
        }

        profile = cls.objects.filter(id=id).update(name = request['name'], accesses = access_list)

        return profile





class Access(models.Model):
    module = models.CharField(max_length=100)
    access = models.JSONField(default='{}')

    def __str__(self):
        return self.module