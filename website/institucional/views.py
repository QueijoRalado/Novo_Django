from django.shortcuts import render
from website.institucional.models import Slideshow

# Create your views here.
def home(request):
    slideshows = Slideshow.objects.all()
    #print(slideshows)
    return render(request,'index.html',{'slideshows':slideshows})    
    

def contato(request):
    nome='Vitor'
    return render(request, 'contato.html', {'nome': nome})