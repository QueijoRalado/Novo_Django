from django.shortcuts import render
from website.institucional.models import Slideshow

# Create your views here.
def home(request):
    slideshows = Slideshow.objects.all()
    #print(slideshows)
    return render(request,'index.html',{'slideshows':slideshows})    
    

def mestres(request):
    return render(request, 'mestres/index.html')