from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return HttpResponse(f"<h1>Hello</h1>")


@login_required
def home(request):
    return render(request, "area_restrita.html")

def index(request):
    return render(request,'./index.html') 