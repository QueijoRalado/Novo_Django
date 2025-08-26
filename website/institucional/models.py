from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class Slideshow(models.Model):
    imagem = models.ImageField(verbose_name ="Imagem", upload_to='slideshow/')
    titulo = models.CharField(verbose_name ="titulo",max_length=50, blank=True, null=True,)
    alt = models.CharField(verbose_name ="Alternative",max_length=100, blank=True, null=True,)
    descricao = models.TextField("Descrição",  blank=True, null= True)

    class Meta:
        verbose_name_plural = 'SlideShow'
        verbose_name = 'SlideShow'
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo

# class Users(AbstractUser):
#     nome = models.CharField(max_length=100)
#     avatar = models.ImageField(verbose_name ="Avatar", upload_to='avatar/')
    
#     class Meta:
#         verbose_name_plural = 'usuarios'
#         verbose_name = 'usuario'
#         ordering = ('nome',)
            
#     def __str__(self):
#         return self.nome    

# class Mestre(models.Model):
#     #usuario = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='mestre_profile')
#     nome = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     ativo = models.BooleanField(default=True)

#     class Meta:
#         verbose_name_plural = 'mestres'
#         verbose_name = 'mestre'
#         ordering = ('nome',)

#     def __str__(self):
#         return self.user.nome

    
                


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nome
    


# from django.contrib.auth.models import AbstractUser

# class Users(AbstractUser):
#     choices_cargo = (
#         ('V','Vendedor'),
#         ('G', 'Gerente')
#     )
#     cargo = models.CharField(max_length=1, choices=choices_cargo)