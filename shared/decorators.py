from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from echos.models import Echo
from users.models import Profile
from waves.models import Wave


def user_validation(func):
    def wrapper(*args, **kwargs):
        user = args[0].user
        username = kwargs.get('username')
        profile_user = User.objects.get(username=username)
        profile = Profile.objects.get(user=profile_user)
        if user != profile.user:
            return HttpResponseForbidden('¡No puedes modificar el perfil de otro usuario!')
        return func(*args, **kwargs)

    return wrapper


def echo_validation(func):
    def wrapper(*args, **kwargs):
        user = args[0].user
        echo = Echo.objects.get(pk=kwargs['pk'])
        if user != echo.user:
            return HttpResponseForbidden('¡No puedes editar el echo de otro usuario!')
        return func(*args, **kwargs)

    return wrapper


def wave_validation(func):
    def wrapper(*args, **kwargs):
        user = args[0].user
        wave = Wave.objects.get(pk=kwargs['pk'])
        if user != wave.user:
            return HttpResponseForbidden('¡No puedes editar el wave de otro usuario!')
        return func(*args, **kwargs)

    return wrapper
