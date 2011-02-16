import datetime
from django import forms
from diversity.models import *

ANOS_CHOICES = [(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]

class DiversityForm(forms.Form):
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),
             required=False, empty_label="Todos los Paises")
    lugar = forms.CharField(widget = forms.SelectMultiple, required=False) 
