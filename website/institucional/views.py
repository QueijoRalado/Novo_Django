from django.shortcuts import render, get_object_or_404, redirect
from website.institucional.models import Slideshow
from .models import Pessoa, Usuario
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def home(request):
    slideshows = Slideshow.objects.all()
    return render(request,'index.html',{'slideshows':slideshows})   

def cadastro(request):
    messages.add_message(request, constants.SUCCESS, 'Página carregada com sucesso')
    return render(request,'cadastro.html') 


def cadastro_adicionar(request):
    if request.method == 'POST':
        primeiroNome_value = request.POST.get('primeiroNome')
        segundooNome_value = request.POST.get('segundoNome')
        username_value = request.POST.get('username')
        email_value = request.POST.get('email')
        senha_value = request.POST.get('senha')
        senha2_value = request.POST.get('senha2')
        if (senha_value!=senha2_value):
            messages.add_message(request, constants.ERROR, 'SEU BOSTA')
            return render(request,'cadastro.html') 

            #return HttpResponse(f"<script>alert('Seu bosta!!!')</script>")
        
        
        print(primeiroNome_value)
        print(segundooNome_value)

        #ANTES DE SALVAR VERIFICAR SE O USUARIO JA EXISTE
        novo_usuario_instancia = Usuario.objects.filter(email=email_value).filter(nickname=username_value)
        print(novo_usuario_instancia)

        if (novo_usuario_instancia):
            return HttpResponse(f"<h1>Já EXITE {primeiroNome_value} {segundooNome_value}!</h1> <script>alert('JA EXISTE')</script>")
        
        
        #REALIZAR O PROCEDIMENTO PARA SALVAR
        novo_usuario_instancia = Usuario(nome = f'{primeiroNome_value} {segundooNome_value}',
                                        nickname = username_value,
                                        email = email_value,
                                        senha = senha_value)
        novo_usuario_instancia.save()
        return redirect('home')
        #return HttpResponse(f"<h1>Hello {primeiroNome_value} {segundooNome_value}!</h1> <script>alert('Usuário cadastrado com sucesso')</script>")
        

def mestres(request):
    return render(request, 'mestres/index.html')

def detalhes(request):
    return render(request, 'mestres/detalhesCampanha.html')


def jogadores(request):
    return render(request, 'jogadores/index.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})


def pessoa_detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoa_detalhe.html', {'pessoa': pessoa})