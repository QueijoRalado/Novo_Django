from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return HttpResponse(f"<h1>Hello</h1>")


@login_required
def home(request):
    return render(request, "index-area-restrita.html")

def mestres(request):
    return render(request, 'mestres/index.html')

def detalhes(request):
    return render(request, 'mestres/detalhesCampanha.html')

def sessoes(request):
    return render(request, 'mestres/sessoes .html')


def jogadores(request):
    return render(request, 'jogadores/index.html')


def meus_personagens(request):
    return render(request, 'personagens/index.html')


def cadastrar_personagem(request):
    return render(request, 'personagens/cadastrar.html')

def editar_personagem(request, id):
    #procurar no BD o personagem do ID que foi passado.
    return render(request, 'personagens/editar.html')
    