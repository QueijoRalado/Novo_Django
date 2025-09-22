from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import Personagem

# Create your views here.
# def home(request):
#     return HttpResponse(f"<h1>Hello</h1>")


@login_required
def home(request):
    return render(request, "index-area-restrita.html")


@login_required
def meus_personagens(request):
    meus_personagens = Personagem.objects.filter(usuario=request.user).order_by('nome_personagem')

    return render(request, 'personagens/index.html', {'personagens': meus_personagens})


@login_required
def cadastrar_personagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_personagem')
        avatar = request.FILES.get('avatar_personagem')
        raca = request.POST.get('raca')
        classe = request.POST.get('classe')
        historia = request.POST.get('historia')

        personagem = Personagem.objects.create(
            usuario=request.user,
            nome_personagem=nome,
            avatar_personagem=avatar,
            raca=raca,
            classe=classe,
            historia=historia
        )
        messages.success(request, f'Personagem {personagem.nome_personagem} cadastrado com sucesso!')
        return redirect('meus_personagens')
    return render(request, 'personagens/cadastrar.html')

@login_required
def editar_personagem(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    if request.method == 'POST':
        personagem.nome_personagem = request.POST.get('nome_personagem')
        if request.FILES.get('avatar_personagem'):
            personagem.avatar_personagem = request.FILES.get('avatar_personagem')
        personagem.raca = request.POST.get('raca')
        personagem.classe = request.POST.get('classe')
        personagem.historia = request.POST.get('historia')
        personagem.save()
        messages.success(request, f'Personagem {personagem.nome_personagem} atualizado com sucesso!')
        return redirect('meus_personagens')
    return render(request, 'personagens/editar.html', {'personagem': personagem})

@login_required
def detalhes_personagem(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    return render(request, 'personagens/detalhes.html', {'personagem': personagem})

@login_required
def deletar_personagem(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    if request.method == 'POST':
        personagem.delete()
        messages.success(request, f'Personagem {personagem.nome_personagem} deletado com sucesso!')
        return redirect('meus_personagens')
    return render(request, 'personagens/confirmar_exclusao.html', {'personagem': personagem})


def mestres(request):
    return render(request, 'mestres/index.html')

def detalhes(request):
    return render(request, 'mestres/detalhesCampanha.html')

def sessoes(request):
    return render(request, 'mestres/sessoes .html')


def jogadores(request):
    return render(request, 'jogadores/index.html')