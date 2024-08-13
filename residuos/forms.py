from django import forms
from empresa.models import Empresa
from .models import Residuos

class ResiduosForm(forms.ModelForm):
    class Meta:
        model = Residuos
        fields = ['descricao', 'empresas']
        widgets = {
            'empresas': forms.CheckboxSelectMultiple,
        }