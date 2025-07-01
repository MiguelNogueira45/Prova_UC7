from django import forms
from .models import Lista_FilmesModel


class FilmesForm(forms.ModelForm):
    class Meta:
        model = Lista_FilmesModel
        fields = ['nome', 'status', 'duracao']


# formulario 