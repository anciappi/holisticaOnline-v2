from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from core.models import Terapias
from image_cropping import ImageRatioField
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField


# PERFIL DE USIARIO
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(upload_to='accounts/users', default='core/img/default-img.jpg', verbose_name='imagen')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Pais')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ciudad')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telefono')
    instagram = models.CharField(max_length=50, blank=True, null=True, verbose_name='Instagram')
    facebook = models.CharField(max_length=50, blank=True, null=True, verbose_name='Facebook')
    twitter = models.CharField(max_length=50, blank=True, null=True, verbose_name='Twitter')
    description = RichTextField(blank=True, null=True, verbose_name='Descripcion')
    titulo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Titulo')
    terapias = models.ManyToManyField(Terapias, blank=True, verbose_name='Terapias')

    register = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    

#FUNCION PARA CREAR UN PERFIL CUANDO SE CREA UN USUARIO
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#FUNCION PARA GUARDAR EL PERFIL EN LA BASE DE DATOS
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)