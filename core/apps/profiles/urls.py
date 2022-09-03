from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    #path('', views.Home, name='modify'),
    path('profiles/', include([
        path('modify', views.Modify, name='modify'),
    ])),
]