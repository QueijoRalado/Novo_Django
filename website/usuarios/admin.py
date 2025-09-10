
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.utils.html import format_html
from django.conf import settings

#admin.site.register(Mestre, MestreAdmin)

# class UsuarioModelAdmin(admin.ModelAdmin):
#     list_display = ( 'nome','avatar_img','nickname', 'email', 'data_nascimento', 'criado_em')
#     #prepopulated_fields = {'slug': ('nickname','nome')}

#     list_filter = ('criado_em', 'atualizado_em')
#     search_fields = ('nickname','nome', 'email', 'eh_mestre','eh_jogador','bio','ativo', )
#     ordering = ('nome','nickname')
#     readonly_fields = ('criado_em', 'atualizado_em')
#     fieldsets = (
#         ('Informações Pessoais', {
#             'fields': ('avatar','nickname','nome', 'email','senha', 'eh_mestre','eh_jogador','bio', 'data_nascimento')
#         }),
#         ('Timestamps', {
#             'fields': ('criado_em', 'atualizado_em'),
#             'classes': ('collapse',),
#         }),
#     )
#     def avatar_img(self,obj):
#         return format_html('<a href="{0}{1}" target="_blank"><img width="60px" src="{0}{1}" alt="avatar" /></a>', settings.MEDIA_URL,obj.avatar)
    
#     avatar_img.allow_tags = True
#     avatar_img.short_description = 'Avatar'

admin.site.register(Usuario)
#admin.site.register(Usuario, UsuarioModelAdmin)