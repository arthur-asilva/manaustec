from django.shortcuts import render, redirect
from .models import Access, Profile
from injections.strategies import AccessValidation

@AccessValidation('users')
def Modify(request):

    profile = request.GET.get('p', None)

    data = {
        'user_access': Access.objects.filter(module='users'),
        'profiles': Profile.objects.all().order_by('name')
    }
    
    if profile is not None:
        data['profile'] = Profile.objects.get(id=profile)

    if request.method == 'POST':
        if profile is None:
            Profile.create(request.POST)
        else:
            Profile.update(data['profile'].id, request.POST)
            return redirect('http://localhost:8000/profiles/modify')

    return render(request, 'profiles/add.html', data)
