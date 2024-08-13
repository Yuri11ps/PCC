from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from rolepermissions.checkers import has_role
from rolepermissions.decorators import has_permission_decorator
from empresa.models import Empresa
from .models import Rota
from .forms import RotaForm

@has_permission_decorator('listar_rota')
def listMap(request):
    rotas = Rota.objects.all()

    context = {
        'rotas' : rotas,
    }
    
    return render(request, 'rota/mapaRota.html', context)

@has_permission_decorator('listar_rota')
def list(request, empresa_id=None):
    title = "Rotas"
    if empresa_id == "None":
        if has_role(request.user, 'empresa'):
            empresa = Empresa.objects.get(responsavel=request.user)
            rotas = Rota.objects.filter(empresa=empresa)
            empresa_id = empresa.id
        else:
            rotas = Rota.objects.all()
        tem = False
    else:
        tem = True
        empresa = Empresa.objects.get(id=empresa_id)
        rotas = Rota.objects.filter(empresa=empresa_id)
        title = f'Rotas da empresa: {empresa.nome}'
    
    context = {
        'empresa_id' : empresa_id,
        'tem' : tem,
        'rotas': rotas,
        'title': title,
    }
    return render(request, 'rota/list.html', context)

@has_permission_decorator('adicionar_rota')
def add(request, empresa_id=None):
    if request.method == 'POST':
        form = RotaForm(request.POST, empresa_id=empresa_id)
            
        if form.is_valid():
            form.save()
            messages.success(request, "Rota criada")
            return redirect('listar_rota', None)
        else:
            print(form.errors)
            messages.error(request, "ERRO")
            return redirect('listar_rota', None)
    else:
        form = RotaForm(empresa_id=empresa_id)

    return render(request, 'rota/create.html', {'form': form})

@has_permission_decorator('editar_rota')
def edit(request, rota_id):
    rota = get_object_or_404(Rota, id=rota_id)
    form = RotaForm(instance=rota, empresa_id=rota.empresa.id)

    if request.method == 'POST':
        form = RotaForm(request.POST, instance=rota, empresa_id=rota.empresa.id)
        if form.is_valid():
            form.save()
            return redirect('listar_rota', None)

    context = {
        'form': form,
    }
    return render(request, "rota/edit.html", context)

@has_permission_decorator('deletar_rota')
def delete(request, rota_id):
    rota = get_object_or_404(Rota, pk=rota_id)
    rota.delete()
    return redirect('listar_rota', rota.empresa.id)