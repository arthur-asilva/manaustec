from django.shortcuts import redirect
from apps.users.models import User


def AccessValidation(module):

    def wrapper(func):

        def wrapper_arguments(request, *args, **kwargs):

            user = User.objects.get(id=request.session['auth'])
            module_exists = module.value in list(user.profile.accesses.keys())

            if module_exists:
                accesses = user.profile.accesses[module.value]
                for access in accesses:
                    if func.__name__ == access['view']:
                        return func(request, *args, **kwargs)
                        
            return redirect('http://localhost:8000')

        return wrapper_arguments

    return wrapper