from django.contrib import admin
from website.institucional.models import Pessoa, Usuario , Slideshow
from django.utils.html import format_html
from django.conf import settings

class SlideshowModelAdmin(admin.ModelAdmin):
    list_display = ['titulo','imagem','alt','descricao',]
    search_fields = ('titulo',)



class MestreAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento')

    

#admin.site.register(Mestre, MestreAdmin)

class UsuarioModelAdmin(admin.ModelAdmin):
    list_display = ('avatar_img','nickname', 'nome', 'email', 'cpf', 'telefone', 'data_nascimento', 'criado_em')
    #prepopulated_fields = {'slug': ('nickname','nome')}

    list_filter = ('criado_em', 'atualizado_em')
    search_fields = ('nickname','nome', 'email', 'eh_mestre','eh_jogador','bio', 'cpf', 'telefone','ativo', )
    ordering = ('nome','nickname')
    readonly_fields = ('criado_em', 'atualizado_em')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('avatar','nickname','nome', 'email','senha', 'eh_mestre','eh_jogador','bio', 'cpf', 'data_nascimento', 'telefone', 'endereco',)
        }),
        ('Timestamps', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',),
        }),
    )
    def avatar_img(self,obj):
        return format_html('<a href="{0}{1}" target="_blank"><img width="60px" src="{0}{1}" alt="foto da fachada" /></a>', settings.MEDIA_URL,obj.avatar)
    
    avatar_img.allow_tags = True
    avatar_img.short_description = 'Avatar'

admin.site.register(Pessoa, PessoaModelAdmin)
#admin.site.register(Usuario)
admin.site.register(Usuario, UsuarioModelAdmin)
admin.site.register(Slideshow,SlideshowModelAdmin)