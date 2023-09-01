from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'CNPJ' : forms.TextInput(attrs={'class': 'form-control'}),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control'}),
            'quitado' : forms.CheckboxInput(),
            'stand' : forms.Select(attrs={'class': 'form-control'})
        }