from django.contrib import admin
from website.institucional.models import  Slideshow
from django.utils.html import format_html
from django.conf import settings

class SlideshowModelAdmin(admin.ModelAdmin):
    list_display = ['titulo','imagem','alt','descricao',]
    search_fields = ('titulo',)


admin.site.register(Slideshow,SlideshowModelAdmin)