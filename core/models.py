from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.
class Terapias(models.Model):
    title = models.CharField(max_length=50, unique=True ,verbose_name='Titulo')
    active = models.BooleanField(default=True, verbose_name='Activo')
    subtitle = models.CharField(max_length=50, verbose_name='Subtitulo', blank=True, null=True)
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(upload_to='terapias', verbose_name='Imagen', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Terapia'
        verbose_name_plural = 'Terapias'
        ordering = ['title']


    def __str__(self):
        return self.title



class Tags(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Tag')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Etiquetas'
        verbose_name_plural = 'Etiquetas'
        ordering = ['title']

    def __str__(self):
        return self.title