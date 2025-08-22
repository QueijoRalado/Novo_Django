from django.contrib import admin
from website.institucional.models import Slideshow
from website.institucional.models import Pessoa

class SlideshowModelAdmin(admin.ModelAdmin):
    list_display = ['titulo','imagem','alt','descricao',]
    search_fields = ('titulo',)





class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento')

admin.site.register(Slideshow,SlideshowModelAdmin)    
admin.site.register(Pessoa, PessoaModelAdmin)