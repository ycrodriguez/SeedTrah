from django import forms

from main.models import Prefactura


class PrefacturaForm(forms.ModelForm):
    class Meta:
        model = Prefactura
        fields = ['cantidad', 'lugar_recogida']
        widgets = {
            'lugar_recogida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar de recogida'}),
            'cantidad': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Cantidad a comprar'}),
        }
