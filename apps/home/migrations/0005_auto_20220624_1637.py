# Generated by Django 3.2.13 on 2022-06-24 21:37

import apps.home.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220624_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tituloelectronico',
            name='tsu_titulo_electronico',
        ),
        migrations.AddField(
            model_name='tituloelectronico',
            name='tsu_titulo_electronico_id',
            field=apps.home.models.CloudinaryField(max_length=255, null=True, verbose_name='tsu_titulo_electronico_id'),
        ),
    ]
