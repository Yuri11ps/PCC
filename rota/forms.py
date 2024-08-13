from django import forms
from empresa.models import Empresa
from rota.models import Rota

class RotaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        empresa_id = kwargs.pop('empresa_id', None)
        super(RotaForm, self).__init__(*args, **kwargs)
        if empresa_id != 'None':
            self.fields['empresa'].queryset = Empresa.objects.filter(pk=empresa_id)
            print(Empresa.objects.filter(pk=empresa_id))
            self.fields['empresa'].initial = empresa_id
            self.fields['empresa'].disabled = True
    class Meta:
        model = Rota
        fields = '__all__'