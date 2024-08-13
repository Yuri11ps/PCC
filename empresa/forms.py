from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuario.models import Usuario
from .models import Empresa
from rolepermissions.roles import assign_role

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'password1', 'password2', 'email')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        
        assign_role(user, 'empresa')
        
        if commit:
            user.save()
        
        return user
    
class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ('username', 'email')

class EmpresaCreationForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome', 'email', 'endereco', 'telefone', 'cnpj')

class EmpresaChangeForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Empresa
        fields = ('nome', 'endereco', 'telefone', 'cnpj')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.responsavel:
            self.fields['username'].initial = self.instance.responsavel.username
            self.fields['email'].initial = self.instance.responsavel.email

    def save(self, commit=True):
        empresa = super().save(commit=False)

        if self.instance and self.instance.responsavel:
            usuario = self.instance.responsavel
            usuario.username = self.cleaned_data.get('username')
            usuario.email = self.cleaned_data.get('email')
            if commit:
                usuario.save()

        if commit:
            empresa.save()
        return empresa
