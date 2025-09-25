from django.db import models
from website.usuarios.models import Usuario
 

# Create your models here.
class Classe(models.Model):
    nome_classe = models.CharField(verbose_name ="classe",max_length=100, blank=True, null=True,)

    class Meta:
        verbose_name_plural = 'Classes'
        verbose_name = 'Classe'
        ordering = ('nome_classe',)

    def __str__(self):
        return self.nome_classe

class Personagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    nome_personagem = models.CharField(verbose_name ="personagem",max_length=50, blank=False, null=False,)
    avatar_personagem = models.ImageField(verbose_name ="avatar", upload_to='personagens/')
    raca = models.CharField(verbose_name ="raça",max_length=50, blank=True, null=True,)
    classe = models.ForeignKey(Classe, on_delete=models.DO_NOTHING, blank = True, null = True, related_name="personagens" )
    #classe = models.CharField(verbose_name ="classe",max_length=100, blank=True, null=True,)
    historia = models.TextField(verbose_name ="historia",  blank=True, null= True)

    class Meta:
        verbose_name_plural = 'Personagens'
        verbose_name = 'Personagem'
        ordering = ('nome_personagem',)

    def __str__(self):
        return self.nome_personagem
    
# , upload_to='slideshow/'


