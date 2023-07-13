from django import forms

from .models import Subscribete


class SubscribirForm(forms.ModelForm):
    class Meta:
        model = Subscribete
        fields = ["nombre", "apellido", "correo"]