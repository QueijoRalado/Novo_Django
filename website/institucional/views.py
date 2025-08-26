from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from website.institucional.models import Slideshow
from .models import Pessoa

# Create your views here.
def home(request):
    slideshows = Slideshow.objects.all()
    #print(slideshows)
    return render(request,'index.html',{'slideshows':slideshows})    
    

def mestres(request):
    return render(request, 'mestres/index.html')


def jogadores(request):
    return render(request, 'jogadores/index.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})


def pessoa_detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoa_detalhe.html', {'pessoa': pessoa})