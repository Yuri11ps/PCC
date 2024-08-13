from django import forms
from empresa.models import Empresa
from .models import Equipamentos

class EquipamentosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        empresa_id = kwargs.pop('empresa_id', None)
        super(EquipamentosForm, self).__init__(*args, **kwargs)
        if empresa_id != 'None':
            self.fields['empresa'].queryset = Empresa.objects.filter(pk=empresa_id)
            self.fields['empresa'].initial = empresa_id
            self.fields['empresa'].disabled = True

    class Meta:
        model = Equipamentos
        fields = '__all__'