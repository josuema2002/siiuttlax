# Generated by Django 3.2.13 on 2022-07-14 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0025_auto_20220714_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id_user_student',
        ),
        migrations.AddField(
            model_name='student',
            name='id_user_student_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='electronicdegree',
            name='birth_certificate_electronic_degree',
            field=models.FileField(blank=True, upload_to='filesT/b153081c-c2c5-43d4-8579-01111bba955a', verbose_name='Acta de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='electronicdegree',
            name='curp_electronic_degree',
            field=models.FileField(blank=True, upload_to='filesT/b153081c-c2c5-43d4-8579-01111bba955a', verbose_name='CURP'),
        ),
        migrations.AlterField(
            model_name='electronicdegree',
            name='high_school_certificate_electronic_degree',
            field=models.FileField(blank=True, upload_to='filesT/b153081c-c2c5-43d4-8579-01111bba955a', verbose_name='Certificado de Bachiller'),
        ),
        migrations.AlterField(
            model_name='electronicdegree',
            name='small_photo_bw_electronic_degree',
            field=models.FileField(blank=True, upload_to='filesT/b153081c-c2c5-43d4-8579-01111bba955a', verbose_name='Foto Infantil B/N'),
        ),
        migrations.AlterField(
            model_name='electronicdegree',
            name='small_photo_color_electronic_degree',
            field=models.FileField(blank=True, upload_to='filesT/b153081c-c2c5-43d4-8579-01111bba955a', verbose_name='Foto Infantil Color'),
        ),
        migrations.AlterField(
            model_name='electronicdegree',
            name='tsu_electronic_degree',
            field=models.FileField(blank=True, upload_to='filesT/b153081c-c2c5-43d4-8579-01111bba955a', verbose_name='TSU'),
        ),
    ]
