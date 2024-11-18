from django import forms

from .models import Profile


class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio')
