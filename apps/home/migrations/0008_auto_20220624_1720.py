# Generated by Django 3.2.13 on 2022-06-24 22:20

import apps.home.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_id_alumno_titulo_electronico_id_tituloelectronico_id_alumno_titulo_electronico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tituloelectronico',
            name='acta_nacimiento_titulo_electronico',
        ),
        migrations.RemoveField(
            model_name='tituloelectronico',
            name='certificado_bachiller_titulo_electronico',
        ),
        migrations.RemoveField(
            model_name='tituloelectronico',
            name='curp_titulo_electronico',
        ),
        migrations.RemoveField(
            model_name='tituloelectronico',
            name='foto_infantil_color_titulo_electronico',
        ),
        migrations.RemoveField(
            model_name='tituloelectronico',
            name='tsu_titulo_electronico',
        ),
        migrations.AlterField(
            model_name='tituloelectronico',
            name='foto_infantil_bn_titulo_electronico',
            field=apps.home.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
