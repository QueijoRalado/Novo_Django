from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from website.institucional.models import Slideshow
from .models import Pessoa
from django.http import HttpResponse

# Create your views here.
def home(request):
    slideshows = Slideshow.objects.all()
    return render(request,'index.html',{'slideshows':slideshows})   

def cadastro(request):
    return render(request,'cadastro.html') 


def cadastro_adicionar(request):
   if request.method == 'POST':
    field1_value = request.POST.get('fname')
    field2_value = request.POST.get('lname')

    print(field1_value)
    print(field2_value)
    
    #REALIZAR O PROCEDIMENTO PARA SALVAR

    return HttpResponse(f"<h1>Hello {field1_value} {field2_value}!</h1> <script>alert('deu certo')</script>")
        

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