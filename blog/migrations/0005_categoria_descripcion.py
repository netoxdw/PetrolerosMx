# Generated by Django 5.0.1 on 2024-02-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_alter_post_imagen_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='Meta descripción'),
        ),
    ]
