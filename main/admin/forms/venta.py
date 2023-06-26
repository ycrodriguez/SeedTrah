from django import forms
from main.models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

    def clean(self):
        cleaned_data = super(VentaForm, self).clean()
        prefactura = cleaned_data.get('prefactura')
        return cleaned_data
