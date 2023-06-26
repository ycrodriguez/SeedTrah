from django import forms
from django.forms.utils import ErrorList

from main.models import Producto


class ProductoFormAdmin(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def clean(self):
        cantidad_existente = self.cleaned_data['cantidad_existente']
        almacen = self.cleaned_data['almacen']
        cant_productos = 0
        productos = Producto.objects.filter(almacen=almacen)
        if productos:
            for p in productos:
                cant_productos += p.cantidad_existente
        cant_productos += cantidad_existente
        if cant_productos > almacen.capacidad:
            self.errors['cantidad_existente'] = ErrorList(['Capacidad del almacen superada'])
        return self.cleaned_data
