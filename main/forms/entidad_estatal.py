from django import forms

from main.models import EntidadEstatal


class EntidadEstatalForm(forms.ModelForm):
    class Meta:
        model = EntidadEstatal
        fields = ['numero_inscripcion', 'tipo']
        widgets = {
            'numero_inscripcion': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Número de inscripción'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo'})
        }
