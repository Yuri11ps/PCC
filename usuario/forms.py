from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from rolepermissions.roles import assign_role

class UsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario        
        fields = ('username', 'nome', 'email', 'cpf', 'endereco', 'telefone', 'is_superuser','password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        
        if user.is_superuser:
            user.is_superuser = True
            user.is_staff = True
            assign_role(user, 'admin')
        else:
            assign_role(user, 'usuario')
        if commit:
            user.save()
        
        return user

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ('nome', 'email', 'endereco', 'telefone', 'cpf', 'is_superuser')

    def save(self, commit=True):
        user = super().save(commit=False)

        if user.is_superuser:
            user.is_superuser = True
            user.is_staff = True
            assign_role(user, 'admin')
        else:
            assign_role(user, 'usuario')
        
        if commit:
            user.save()
        
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'empresa') and self.instance.empresa is not None:
            self.fields.pop('is_superuser')
        self.fields.pop('password')