from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('cadastro/',views.cadastro, name='cadastro'),
    #path('login/',views.login, name='login'),
    #path('login/entrar/',views.login_adicionar, name='login_adicionar'),

    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),

    # path('cadastro/add/',views.cadastro_adicionar, name='cadastro_adicionar'),
    path('mestres/',views.mestres, name='mestres'),
    path('mestres/detalhes',views.detalhes, name='detalhes'),
    path('mestres/sessoes',views.sessoes, name='sessoes'),
    path('jogadores/',views.jogadores, name='jogadores'),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/<int:id>/', views.pessoa_detalhe, name='pessoa_detalhe'),
]

