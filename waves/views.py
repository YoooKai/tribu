from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from shared.decorators import wave_validation
from waves.forms import EditWaveForm
from waves.models import Wave


@login_required
@wave_validation
def edit_wave(request, pk):
    wave = Wave.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditWaveForm(request.POST, instance=wave)
        if form.is_valid():
            form.save()
            return redirect('echos:echo-list')
    else:
        form = EditWaveForm(instance=wave)
    return render(request, 'waves/edit-wave.html', {'wave': wave, 'form': form})


@login_required
@wave_validation
def delete_wave(request, pk):
    wave = Wave.objects.get(pk=pk)
    if request.method in ['POST', 'GET']:
        wave.delete()
        return redirect('echos:echo-list')

    return render(request, 'waves/confirm-delete.html', {'wave': wave})
