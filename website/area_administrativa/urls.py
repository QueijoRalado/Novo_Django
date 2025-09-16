from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home_area_restrita'),
    # path('meus-personagens/',views.meus_personagens, name='meus_personagens'),
    path('cadastrar_personagem/',views.cadastrar_personagem, name='cadastrar_personagem'),
    path('mestres/',views.mestres, name='mestres'),
    path('mestres/detalhes',views.detalhes, name='detalhes'),
    path('mestres/sessoes',views.sessoes, name='sessoes'),
    path('jogadores/',views.jogadores, name='jogadores'),
]