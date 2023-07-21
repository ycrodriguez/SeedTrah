from django import forms

from main.models import PersonaNatural


class PersonaNaturalForm(forms.ModelForm):
    class Meta:
        model = PersonaNatural
        fields = ['ci']
        widgets = {
            'ci': forms.NumberInput(attrs={'class': 'form-control persona-natural', 'placeholder': 'Carne de Identidad',
                                           'id': 'persona-natural-ci'}),
        }
