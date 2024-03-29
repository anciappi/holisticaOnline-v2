# Generated by Django 4.2.7 on 2024-01-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Tag')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Etiquetas',
                'verbose_name_plural': 'Etiquetas',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Terapias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Titulo')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('subtitle', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subtitulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='terapias', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Terapia',
                'verbose_name_plural': 'Terapias',
                'ordering': ['title'],
            },
        ),
    ]
