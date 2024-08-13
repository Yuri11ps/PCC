from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from empresa.models import Empresa
from usuario.models import Usuario
from .forms import EmpresaCreationForm, UsuarioCreationForm, EmpresaChangeForm
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('listar_empresa')
def list(request):
    empresas = Empresa.objects.all()
    context = {
        'empresas': empresas,
    }
    return render(request, 'empresa/list.html', context)

@has_permission_decorator('adicionar_empresa')
def add(request):
    if request.method == 'POST':
        formempresa = EmpresaCreationForm(request.POST)
        formusuario = UsuarioCreationForm(request.POST)
        if formempresa.is_valid() and formusuario.is_valid:
            user = formusuario.save()
            formempresa.instance.responsavel = user
            formempresa.save()

            messages.success(request, "Empresa criada com sucesso. Faça login.")
            return redirect('listar_empresa')
        else:
            messages.error(request, "Erro ao validar o formulário. Verifique os dados e tente novamente.")
    else:
        formempresa = EmpresaCreationForm()
        formusuario = UsuarioCreationForm()
    
    return render(request, 'empresa/create.html', {'formempresa': formempresa, 'formusuario': formusuario})

@has_permission_decorator('editar_empresa')
def edit(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        form = EmpresaChangeForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, "Empresa atualizada com sucesso.")
            return redirect('listar_empresa')
        else:
            messages.error(request, "Erro ao validar o formulário. Verifique os dados e tente novamente.")
    else:
        form = EmpresaChangeForm(instance=empresa)

    return render(request, "empresa/edit.html", {'form': form})

@has_permission_decorator('deletar_empresa')
def delete(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    responsavel = get_object_or_404(Usuario, pk=empresa.responsavel.id)
    empresa.delete()
    responsavel.delete()
    return redirect(reverse('listar_empresa'))