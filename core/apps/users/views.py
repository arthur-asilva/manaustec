from django.shortcuts import render, redirect
from apps.profiles.models import Profile
from .models import User
from injections.strategies import AccessValidation
from injections.addons import Module

@AccessValidation(Module.USERS)
def Modify(request):

    user = request.GET.get('u', None)

    data = {
        'profiles': Profile.objects.all().order_by('name'),
        'users': User.objects.all().order_by('name')
    }

    if user is not None:
        data['user'] = User.objects.get(id=user)

    if request.method == 'POST':
        if user is None:
            User.create(request.POST)
        else:
            new_request = request.POST.copy()
            new_request['id'] = user
            User.update(new_request)
        return redirect('http://localhost:8000/users/modify')

    return render(request, 'users/add.html', data)




def Login(request):

    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'], password=request.POST['password'])
        if user.exists:
            request.session['auth'] = user.first().id
            return redirect('http://localhost:8000/users/modify')

    return render(request, 'login.html')