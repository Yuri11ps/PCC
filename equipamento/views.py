from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rolepermissions.checkers import has_role
from rolepermissions.decorators import has_permission_decorator
from empresa.models import Empresa
from .models import Equipamentos
from .forms import EquipamentosForm

@has_permission_decorator('listar_equipamento')
def list(request, empresa_id=None):
    title = "Equipamentos"

    if empresa_id == "None":
        if has_role(request.user, 'empresa'):
            empresa = Empresa.objects.get(responsavel=request.user)
            equipamentos = Equipamentos.objects.filter(empresa=empresa)
            empresa_id = empresa.id
        else:
            equipamentos = Equipamentos.objects.all()
    else:
        empresa = Empresa.objects.get(id=empresa_id)
        equipamentos = Equipamentos.objects.filter(empresa=empresa_id)
        title = f'Equipamentos da empresa: {empresa.nome}'
    
    context = {
        'empresa_id' : empresa_id,
        'equipamentos': equipamentos,
        'title': title,
    }
    return render(request, 'equipamento/list.html', context)

@has_permission_decorator('adicionar_equipamento')
def add(request, empresa_id=None):
    if request.method == 'POST':
        form = EquipamentosForm(request.POST, empresa_id=empresa_id)
        if form.is_valid():
            form.save()
            messages.success(request, "equipamentos criada")
            return redirect('listar_equipamento', empresa_id)
        else:
            messages.error(request, "ERRO")
            return redirect('listar_equipamento', None)
    else:
        form = EquipamentosForm(empresa_id=empresa_id)

    return render(request, 'equipamento/create.html', {'form': form})

@has_permission_decorator('editar_equipamento')
def edit(request, equipamento_id):
    equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
    if has_role(request.user, 'admin'):
        empresa_id = 'None'
    else:
        empresa_id = equipamento.empresa.id

    form = EquipamentosForm(instance=equipamento, empresa_id=empresa_id)

    if request.method == 'POST':
        form = EquipamentosForm(request.POST, empresa_id=empresa_id, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipamentos editado")
            return redirect('listar_equipamento', equipamento.empresa.id)
        else:
            messages.error(request, "ERRO")
            return redirect('listar_equipamento', None)
    context = {
        'form': form,
    }
    return render(request, "equipamento/edit.html", context)

@has_permission_decorator('deletar_equipamento')
def delete(request, equipamento_id):
    equipamento = get_object_or_404(Equipamentos, pk=equipamento_id)
    equipamento.delete()
    return redirect('listar_equipamento', equipamento.empresa.id)