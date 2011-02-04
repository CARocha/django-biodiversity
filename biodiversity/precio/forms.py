from django import forms
from models import *

class PrecioForm(forms.Form):
    fecha_inicio = forms.DateField()
    fecha_final = forms.DateField()
    pais = models.MultipleChoiceField(required=False,
            choices = Pais.objects.all())
    zona = forms.MultipleChoiceField(required = False, 
            choices = Lugar.objects.all()) 
