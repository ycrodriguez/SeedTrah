from django import forms

from main.models import Prefactura


class PrefacturaForm(forms.ModelForm):
    class Meta:
        model = Prefactura
        fields = ['cantidad']
        widgets = {
            'cantidad': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Cantidad a comprar'}),
        }
