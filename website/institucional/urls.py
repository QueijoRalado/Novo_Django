from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('mestres/index.html',views.mestres, name='mestres'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
]
