from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from echos.models import Echo
from shared.decorators import echo_validation
from waves.models import Wave

from .forms import AddEchoForm, AddWaveForm, EditEchoForm

User = get_user_model()


@login_required
def echo_list(request):
    form = AddEchoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('echos:echo-list')
    echos = Echo.objects.all().order_by('-created_at')
    return render(request, 'echos/echo-list.html', {'echos': echos, 'form': form})


@login_required
def echo_detail(request, pk):
    echo = Echo.objects.get(pk=pk)
    waves = echo.waves.order_by('-created_at')
    waves_to_show = list(waves[:5])
    show_see_all_button = waves.count() > 5
    return render(
        request,
        'echos/echo-detail.html',
        {
            'echo': echo,
            'waves': waves_to_show,
            'show_see_all_button': show_see_all_button,
        },
    )


@login_required
def add_echo(request):
    if request.method == 'POST':
        form = AddEchoForm(request.POST)
        if form.is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm()
    return render(request, 'echos/add-echo.html', {'form': form})


@login_required
@echo_validation
def edit_echo(request, pk):
    echo = Echo.objects.get(pk=pk)
    if request.method == 'POST':
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            form.save()
            return redirect('echos:echo-list')
    else:
        form = EditEchoForm(instance=echo)
    return render(request, 'echos/edit-echo.html', {'echo': echo, 'form': form})


@login_required
@echo_validation
def delete_echo(request, pk):
    echo = Echo.objects.get(pk=pk)
    if request.method in ['POST', 'GET']:
        echo.delete()
        return redirect('echos:echo-list')
    return render(request, 'echos/confirm-delete.html', {'echo': echo})


@login_required
def add_wave(request, pk):
    echo = Echo.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddWaveForm(request.POST)
        if form.is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = echo
            wave.save()
            return redirect('echos:echo-detail', pk=echo.pk)
    else:
        form = AddWaveForm()
    return render(request, 'echos/add-wave.html', {'form': form, 'echo': echo})


@login_required
def wave_list(request, pk):
    echo = Echo.objects.get(pk=pk)
    waves = Wave.objects.filter(echo=echo).order_by('-created_at')
    return render(request, 'echos/wave-list.html', {'echo': echo, 'waves': waves})
