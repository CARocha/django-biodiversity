from django import forms
from models import * 

class PrecioSeleccionadorForm(forms.Form):
    lugar = forms.ModelChoiceField(queryset=Lugar.objects.all())

class PrecioConsumidorInlineForm(forms.ModelForm):
    zona = forms.ModelChoiceField(queryset=Lugar.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = PrecioConsumidor

class PrecioProductorInlineForm(forms.ModelForm):
    zona = forms.ModelChoiceField(queryset=Lugar.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Precio
