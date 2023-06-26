from django import forms

from main.models import Cliente, Empresa


class ClienteForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(Empresa.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Empresa'}))

    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'empresa', 'tipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'tipo': forms.Select(attrs={'class': 'form-control'})
        }
