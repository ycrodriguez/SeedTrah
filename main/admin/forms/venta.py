from django import forms
from django.forms.utils import ErrorList

from main.models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

    def clean(self):
        cleaned_data = super(VentaForm, self).clean()
        cliente = cleaned_data.get('cliente')
        cant_vendida = cleaned_data.get('cant_vendida')
        cant_producto = cleaned_data.get('producto').count()
        try:
            if cliente.persona_natural:
                if cant_vendida > cant_producto:
                    self._errors['cant_vendida'] = ErrorList(
                        ['Una persona natural no puede comprar más de 1 quintal de cada tipo'])
        except:
            return cleaned_data
        return cleaned_data
