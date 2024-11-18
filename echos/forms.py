from django import forms

from waves.models import Wave

from .models import Echo


class AddEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update(
            {
                'class': 'form-control form-control-xs',
                'placeholder': 'Write your echo...',
            }
        )


class EditEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)


class AddWaveForm(forms.ModelForm):
    class Meta:
        model = Wave
        fields = ['content']
