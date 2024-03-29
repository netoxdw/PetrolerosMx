# Generated by Django 5.0 on 2023-12-27 21:10

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=110, verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('imagen', models.URLField(verbose_name='Imagen')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No publicado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Feacha de creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
