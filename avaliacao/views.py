from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from empresa.models import Empresa
from .models import Avaliacao
from .forms import AvaliacaoForm
from rolepermissions.decorators import has_permission_decorator
from rolepermissions.checkers import has_role

@has_permission_decorator('listar_avaliacao')
def list(request, empresa_id=None):
    if empresa_id == "None":
        avaliacoes = Avaliacao.objects.all()
        title = "Avaliações"
        tem = False
    else:
        tem = True
        empresa = Empresa.objects.get(id=empresa_id)
        avaliacoes = Avaliacao.objects.filter(empresa=empresa_id)
        title = f'Avaliações da empresa: {empresa.nome}'

    context = {
        'empresa_id' : empresa_id,
        'title' : title,
        'tem' : tem,
        'avaliacoes': avaliacoes,
    }
    return render(request, 'avaliacao/list.html', context)

@has_permission_decorator('adicionar_avaliacao')
def add(request, empresa_id=None):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, empresa_id=empresa_id)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            messages.success(request, "Avaliação criada")
            return redirect('listar_avaliacao', avaliacao.empresa.id)
        else:
            messages.error(request, "ERRO")
            return redirect('listar_avaliacao', None)
    else:
        form = AvaliacaoForm(empresa_id=empresa_id)

    return render(request, 'avaliacao/create.html', {'form': form})

@has_permission_decorator('editar_avaliacao')
def edit(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    if has_role(request.user, 'admin'):
        empresa_id = 'None'
    else:
        empresa_id = avaliacao.empresa.id

    form = AvaliacaoForm(instance=avaliacao,empresa_id=empresa_id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, empresa_id=empresa_id, instance=avaliacao)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.save()
            messages.success(request, "Avaliação Editada")
            return redirect('listar_avaliacao', avaliacao.empresa.id)
        else:
            messages.error(request, "ERRO")
            return redirect('listar_avaliacao', None)

    context = {
        'form': form,
    }
    return render(request, "avaliacao/edit.html", context)

@has_permission_decorator('deletar_avaliacao')
def delete(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)
    avaliacao.delete()
    return redirect('listar_avaliacao', None)