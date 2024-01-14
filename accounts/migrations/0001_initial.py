# Generated by Django 4.2.7 on 2024-01-06 02:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='core/img/default-img.jpg', upload_to='accounts/users', verbose_name='imagen')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pais')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('instagram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Instagram')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=50, null=True, verbose_name='Twitter')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Titulo')),
                ('register', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('terapias', models.ManyToManyField(blank=True, to='core.terapias', verbose_name='Terapias')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-id'],
            },
        ),
    ]