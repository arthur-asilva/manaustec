from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Login, name='login'),
    path('users/', include([
        path('modify', views.Modify, name='modify'),
        #path('<slug:slug>/get', views.Get, name='get'),
        #path('<slug:slug>/delete', views.Delete, name='delete'),
    ])),
]