from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_terapeutas_group(sender, instance, created, **kwargs):
    if created:
        try:
            terapeutas = Group.objects.get(name='terapeutas')
        except Group.DoesNotExist:
            terapeutas = Group.objects.create(name='terapeutas')
            pacientes = Group.objects.create(name='pacientes')
            administradores = Group.objects.create(name='administradores')
        instance.user.groups.add(terapeutas)