from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from django.utils.text import slugify
import datetime

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

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    nome = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)  
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField("Biografia", blank=True)     

    eh_mestre = models.BooleanField(default=False)
    eh_jogador = models.BooleanField(default=False)

    senha = models.CharField(max_length=128, blank=False)  # precisa aumentar o tamanho para hash

                                    
    slug = models.SlugField('slug')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)
    
    def check_senha(self, raw_password):
        return check_password(raw_password, self.senha)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nickname or self.username)
            slug = base_slug
            counter = 1
            while Usuario.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'usuários'
        verbose_name = 'usuário'
        ordering = ('-criado_em',)

    def __str__(self):
        return self.nickname


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