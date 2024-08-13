from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from rolepermissions.checkers import has_role
from rolepermissions.decorators import has_permission_decorator
from empresa.models import Empresa
from .models import Residuos
from .forms import ResiduosForm

@has_permission_decorator('listar_residuo')
def list(request, empresa_id=None):
    title = "Residuos"
    if empresa_id == "None":
        residuos = Residuos.objects.all()
    else:
        empresa = Empresa.objects.get(id=empresa_id)
        residuos = Residuos.objects.filter(empresas=empresa_id)
        title = f'Residuos da empresa: {empresa.nome}'
    
    context = {
        'empresa_id' : empresa_id,
        'residuos': residuos,
        'title': title,
    }
    return render(request, 'residuo/list.html', context)

@has_permission_decorator('adicionar_residuo')
def add(request):

    if has_role(request.user, 'admin'):
        empresa_id = None
    else:
        empresa_id = Empresa.objects.get(responsavel=request.user).id
        empresa = Empresa.objects.get(pk=empresa_id)

    if request.method == 'POST':
        form = ResiduosForm(request.POST)
        if form.is_valid():
            residuos = form.save(commit=False)
            residuos.save()
            if empresa_id != None:
                if 'empresas' in form.cleaned_data and empresa in form.cleaned_data['empresas']:
                    residuos.empresas.add(empresa)
            else:
                form.save_m2m()

            return redirect('listar_residuo', None)
    else:
        form = ResiduosForm()
        if empresa_id != None:
            form.fields['empresas'].queryset = Empresa.objects.filter(pk=empresa_id)
            form.fields['empresas'].initial = [empresa_id]
        else:
            form.fields['empresas'].queryset = Empresa.objects.all()

    return render(request, 'residuo/create.html', {'form': form})

@has_permission_decorator('editar_residuo')
def edit(request, residuo_id):
    residuos = get_object_or_404(Residuos, pk=residuo_id)

    if has_role(request.user, 'admin'):
        empresa_id = None
    else:
        empresa = Empresa.objects.get(responsavel=request.user.id)
        empresa_id = empresa.id

    if request.method == 'POST':
        form = ResiduosForm(request.POST, instance=residuos)
        if form.is_valid():
            residuos = form.save(commit=False)
            residuos.save()
            if empresa_id != None:
                if 'empresas' in form.cleaned_data and empresa in form.cleaned_data['empresas']:
                    residuos.empresas.add(empresa)
                else:
                    residuos.empresas.remove(empresa)
            else:
                form.save_m2m()
            return redirect('listar_residuo', None)
    else:
        form = ResiduosForm(instance=residuos)

        if empresa_id != None:
            form.fields['empresas'].queryset = Empresa.objects.filter(pk=empresa_id)
            form.fields['empresas'].initial = [empresa_id] if empresa in residuos.empresas.all() else []
        else:
            form.fields['empresas'].queryset = Empresa.objects.all()

    return render(request, "residuo/edit.html", {'form': form})

@has_permission_decorator('deletar_residuo')
def delete(request, residuo_id):
    residuo = get_object_or_404(Residuos, pk=residuo_id)
    residuo.delete()
    return redirect('listar_residuo', None)