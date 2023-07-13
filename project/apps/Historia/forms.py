from django import forms

from .models import Personaje, Faccion


class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = "__all__"

class FaccionForm(forms.ModelForm):
    class Meta:
        model = Faccion
        fields = "__all__"