from django import forms
from models import * 

class PrecioSeleccionadorForm(forms.Form):
    lugar = forms.ModelChoiceField(queryset=Lugar.objects.all())

class PrecioConsumidorInlineForm(forms.ModelForm):
    zona = forms.ModelChoiceField(queryset=Lugar.objects.all(), widget=forms.Select(attrs={'style': 'display:none'}))

    class Meta:
        model = PrecioConsumidor

class PrecioProductorInlineForm(forms.ModelForm):
    zona = forms.ModelChoiceField(label='zona', queryset=Lugar.objects.all(), 
            widget=forms.Select(attrs={'disabled': 'true'}))


    class Meta:
        model = Precio
