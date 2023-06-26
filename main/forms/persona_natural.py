from django import forms

from main.models import PersonaNatural


class PersonaNaturalForm(forms.ModelForm):
    class Meta:
        model = PersonaNatural
        fields = ['ci']
        widgets = {
            'ci': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Carne de Identidad'}),
        }
