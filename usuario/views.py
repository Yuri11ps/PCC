from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada, faça login")
            return redirect('login')
        else:
            messages.error(request, "ERRO")
            return redirect('registration')
    else:
        form = UsuarioCreationForm()
    
    return render(request, 'registration/registration.html', {'form': form})

class MyLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('listar_empresa')
        return super().dispatch(request, *args, **kwargs)

def sair(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    user = Usuario.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil alterado")
            return redirect('perfil')
        else:
            messages.error(request, "ERRO")
            return redirect('perfil')
    elif request.method == 'GET':
        form = UsuarioChangeForm(instance=user)
        return render(request, 'registration/perfil.html', {'user': user, 'form': form})