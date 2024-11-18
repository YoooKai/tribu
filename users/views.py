from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from echos.models import Echo
from shared.decorators import user_validation

from .forms import EditUserForm


@login_required
def user_profile(request, username):
    profile = User.objects.get(username=username)
    echos = Echo.objects.filter(user=profile)
    show_see_all_button = echos.count() > 5

    return render(
        request,
        'users/user-profile.html',
        {
            'profile': profile,
            'echos': echos[:5],
            'show_see_all_button': show_see_all_button,
        },
    )


@login_required
def my_user_detail(request):
    return redirect('users:user-profile', username=request.user)


@login_required
def user_echos(request, username):
    profile = User.objects.get(username=username)
    echos = Echo.objects.filter(user=profile)

    return render(
        request,
        'users/user-profile.html',
        {
            'profile': profile,
            'echos': echos,
        },
    )


@login_required
@user_validation
def edit_user(request, username):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:user-profile', username=user.username)
        else:
            print('Formulario no válido. Errores:', form.errors)
    else:
        form = EditUserForm(instance=profile)
    return render(request, 'users/edit-user.html', {'form': form})


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user-list.html', {'users': users})
