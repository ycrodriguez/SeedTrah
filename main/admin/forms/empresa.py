from django import forms
from django.forms.utils import ErrorList

from main.models import Empresa


class EmpresaFormAdmin(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    def clean(self):
        phone = self.cleaned_data.get('telefono', None)
        if not phone.isdigit():
            self.errors['telefono'] = ErrorList(['Solo se permiten números'])
        return self.cleaned_data
