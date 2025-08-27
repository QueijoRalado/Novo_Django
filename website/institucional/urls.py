from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cadastro/',views.cadastro, name='cadastro'),
    path('cadastro/add/',views.cadastro_adicionar, name='cadastro_adicionar'),
    path('mestres/',views.mestres, name='mestres'),
    path('mestres/detalhes/campanhas/',views.detalhes, name='detalhes'),
    path('jogadores/',views.jogadores, name='jogadores'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/<int:id>/', views.pessoa_detalhe, name='pessoa_detalhe'),
]
