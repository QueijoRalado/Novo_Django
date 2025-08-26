from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('mestres/index.html',views.mestres, name='mestres'),
    path('jogadores/index.html',views.jogadores, name='jogadores'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/<int:id>/', views.pessoa_detalhe, name='pessoa_detalhe'),
]
