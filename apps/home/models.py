# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class alumno(models.Model):
    matricula_alumno = models.AutoField(primary_key=True)
    id_user_alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_alumno = models.CharField(max_length=50)
    apellido_alumno = models.CharField(max_length=50, default='')
    carrera_alumno = models.CharField(max_length=50)
    correo_alumno = models.EmailField(max_length=50)
    telefono_alumno = models.CharField(max_length=50)
    created_at_alumno = models.DateTimeField(auto_now_add=True)
    updated_at_alumno = models.DateTimeField(auto_now=True)
    titularse_alumno = models.BooleanField(default=False)

class empleado(models.Model):
    matricula_empleado = models.AutoField(primary_key=True)
    id_user_empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    correo_empleado = models.EmailField(max_length=50)
    telefono_empleado = models.CharField(max_length=50)
    created_at_empleado = models.DateTimeField(auto_now_add=True)
    updated_at_empleado = models.DateTimeField(auto_now=True)
    puesto_empleado = models.CharField(max_length=50)
    nivel_academico_empleado = models.CharField(max_length=50)

class certificadoTitulacion(models.Model):
    id_certificado_titulacion = models.AutoField(primary_key=True)
    id_alumno_certificado_titulacion = models.ForeignKey(alumno, on_delete=models.CASCADE)
    plan_estudio_certificado_titulacion = models.CharField(max_length=50)
    periodo_escolar_certificado_titulacion = models.CharField(max_length=50)

class tituloElectronico(models.Model):
    id_titulo_electronico = models.AutoField(primary_key=True)
    id_alumno_titulo_electronico = models.ForeignKey(alumno, on_delete=models.CASCADE)
    foto_infantil_bn_titulo_electronico = models.CharField(max_length=100)
    foto_infantil_color_titulo_electronico = models.CharField(max_length=100)
    curp_titulo_electronico = models.CharField(max_length=50)
    acta_nacimiento_titulo_electronico = models.CharField(max_length=100)
    certificado_bachiller_titulo_electronico = models.CharField(max_length=100)
    tsu_titulo_electronico = models.CharField(max_length=100, null=True)
    status_foto_infantil_bn_titulo_electronico = models.BooleanField(default=False)
    status_foto_infantil_color_titulo_electronico = models.BooleanField(default=False)
    status_curp_titulo_electronico = models.BooleanField(default=False)
    status_acta_nacimiento_titulo_electronico = models.BooleanField(default=False)
    status_certificado_bachiller_titulo_electronico = models.BooleanField(default=False)
    status_tsu_titulo_electronico = models.BooleanField(default=False)
    created_at_titulo_electronico = models.DateTimeField(auto_now_add=True)
    updated_at_titulo_electronico = models.DateTimeField(auto_now=True)

class estadisticasTitulacion(models.Model):
    id_estadisticas_titulacion = models.AutoField(primary_key=True)
    genero_estadisticas_titulacion = models.CharField(max_length=50)
    fecha_init_estadisticas_titulacion = models.DateField()
    fecha_end_estadisticas_titulacion = models.DateField()
    ingreso_estadisticas_titulacion = models.IntegerField()
    egreso_estadisticas_titulacion = models.IntegerField()
    titulados_estadisticas_titulacion = models.IntegerField()
    rezagados_estadisticas_titulacion = models.IntegerField()
    porcentaje_titulados_estadisticas_titulacion = models.BooleanField(default=False)
    # total_estudiantes_estadisticas_titulacion = models.IntegerField()
    # total_titulados_estadisticas_titulacion = models.IntegerField()
    # total_no_titulados_estadisticas_titulacion = models.IntegerField()
    # created_at_estadisticas_titulacion = models.DateTimeField(auto_now_add=True)



    

    