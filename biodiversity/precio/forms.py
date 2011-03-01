from django import forms
from models import *

class PrecioForm(forms.Form):
    fecha_inicio = forms.DateField()
    fecha_final = forms.DateField()
    pais = models.MultipleChoiceField(required=True,
            choices = Pais.objects.all(), initial='Mierda')
    zona = forms.MultipleChoiceField(required = True, 
            choices = Lugar.objects.all()) 

