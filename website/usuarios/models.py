from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models

class Usuario(AbstractUser):
    # Campos adicionais, se quiser
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to="avatar/",   # pasta dentro de MEDIA_ROOT
        blank=True,
        null=True
    )

    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField("Biografia", blank=True)     

    eh_mestre = models.BooleanField(default=False)
    eh_jogador = models.BooleanField(default=True)
                                   
    slug = models.SlugField('slug')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.username)
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
        return f'{self.username}'
