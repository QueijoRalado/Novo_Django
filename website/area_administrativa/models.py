from django.db import models

# Create your models here.


class Personagem(models.Model):
    nome_personagem = models.CharField(verbose_name ="personagem",max_length=50, blank=False, null=False,)
    avatar_personagem = models.ImageField(verbose_name ="avatar")
    raca = models.CharField(verbose_name ="raça",max_length=50, blank=True, null=True,)
    classe = models.CharField(verbose_name ="classe",max_length=100, blank=True, null=True,)
    historia = models.TextField(verbose_name ="historia",  blank=True, null= True)

    class Meta:
        verbose_name_plural = 'Personagens'
        verbose_name = 'Personagem'
        ordering = ('personagem',)

    def __str__(self):
        return self.nome_personagem
    
# , upload_to='slideshow/'