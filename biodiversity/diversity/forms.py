import datetime
from django import forms
from diversity.models import *

ANOS_CHOICES = ((2010,'2010'),(2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'))
TIPO_GRAFO = ((1,'Precio'),(2,'Clima'),(3,'Humedad'))

class DiversityForm(forms.Form):
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),
             required=False, empty_label="Todos los Paises")
    lugar = forms.ModelChoiceField(queryset=Lugar.objects.all(), 
            required=False, empty_label="Todos los Lugares")
    tipo_grafo = forms.ChoiceField(choices=TIPO_GRAFO)
     
