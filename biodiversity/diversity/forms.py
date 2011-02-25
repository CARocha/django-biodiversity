import datetime
from django import forms
from diversity.models import *
from biodiversity.precio.models import *

ANOS_CHOICES = [(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]

class DiversityForm(forms.Form):
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),
             required=False, empty_label="Todos los Paises")
    lugar = forms.CharField(widget = forms.SelectMultiple, required=False) 


class PrecioForm(forms.Form):
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    #pais = forms.ModelChoiceField(queryset=Pais.objects.all(),
    #         required=False, empty_label="Todos los Paises")
    lugar = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, 
                                   queryset=Lugar.objects.all(), required=False) 
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    unidad = forms.ChoiceField(choices=(('nativa', 'Nativa'), 
                                        ('normalizada', 'Normalizada')),
                                        widget=forms.RadioSelect)
    #ModelMultipleChoiceField(widget=forms.SelectMultiple,
    #                queryset=RubroCultivo.objects.all(), label='Rubro Cultivo',
