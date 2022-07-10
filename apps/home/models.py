# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid



# Create your models here.

class alumno(models.Model):
    matricula_alumno = models.CharField(primary_key=True, max_length=15)
    id_user_alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_alumno = models.CharField(max_length=50)
    apellidop_alumno = models.CharField(max_length=50, default='')
    apellidom_alumno = models.CharField(max_length=50, default='')
    carrera_alumno = models.CharField(max_length=50)
    area_carrera_alumno = models.CharField(max_length=50, default='')
    genero_alumno = models.CharField(max_length=50, default='')
    correo_alumno = models.EmailField(max_length=50)
    telefono_alumno = models.CharField(max_length=50)
    created_at_alumno = models.DateTimeField(auto_now_add=True)
    updated_at_alumno = models.DateTimeField(auto_now=True)
    
    estadiasTSU_alumno = models.BooleanField(default=False)
    estadiasIngLic_alumno = models.BooleanField(default=False)

class empleado(models.Model):
    matricula_empleado = models.CharField(primary_key=True, max_length=15)
    id_user_empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_empleado = models.CharField(max_length=50)
    apellido_empleado = models.CharField(max_length=50)
    correo_empleado = models.EmailField(max_length=50)
    telefono_empleado = models.CharField(max_length=50)
    created_at_empleado = models.DateTimeField(auto_now_add=True)
    updated_at_empleado = models.DateTimeField(auto_now=True)
    puesto_empleado = models.CharField(max_length=50)
    nivel_academico_empleado = models.CharField(max_length=50)
    #1 = docente
    #2 = asistente
    #3 = administrativo
    #4 = jefe de area
    #5 = director de carrera
    #6 = director de academico
    #7 = rector

class certificadoTitulacion(models.Model):
    id_certificado_titulacion = models.AutoField(primary_key=True)
    matricula_alumno_titulacion = models.ForeignKey(alumno, on_delete=models.CASCADE)
    nombre_alumno_titulacion = models.CharField(max_length=50, default='')
    apellidop_alumno_titulacion = models.CharField(max_length=50, default='')
    apellidom_alumno_titulacion = models.CharField(max_length=50, default='')
    anio_plan_estudios_titulacion = models.IntegerField(default=0)
    periodo_escolar_init_titulacion = models.CharField(max_length=50, default='')
    periodo_escolar_end_titulacion = models.CharField(max_length=50, default='')
    carrera_titulacion = models.CharField(max_length=50, default='')
    area_carrera_titulacion = models.CharField(max_length=50, default='')
    tipo_carrera_titulacion = models.CharField(max_length=50, default='')
    jefe_area_servicios_escolares_titulacion = models.CharField(max_length=50, default='')
    director_carrera_titulacion = models.CharField(max_length=50, default='')
    calificaciones_titulacion = models.TextField(default='')

idFileUser = uuid.uuid4()
class tituloElectronico(models.Model):
    id_titulo_electronico = models.AutoField(primary_key=True)
    id_alumno_titulo_electronico = models.ForeignKey(alumno, on_delete=models.CASCADE, default='')
    foto_infantil_bn_titulo_electronico = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Foto Infantil B/N')
    foto_infantil_color_titulo_electronico = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Foto Infantil Color')
    curp_titulo_electronico = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='CURP')
    acta_nacimiento_titulo_electronico =  models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Acta de Nacimiento')
    certificado_bachiller_titulo_electronico = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Certificado de Bachiller')
    tsu_titulo_electronico = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='TSU')
    status_foto_infantil_bn_titulo_electronico = models.BooleanField(blank=True, null=True)
    status_foto_infantil_color_titulo_electronico = models.BooleanField(blank=True, null=True)
    status_curp_titulo_electronico = models.BooleanField(blank=True, null=True)
    status_acta_nacimiento_titulo_electronico = models.BooleanField(blank=True, null=True)
    status_certificado_bachiller_titulo_electronico = models.BooleanField(blank=True, null=True)
    status_tsu_titulo_electronico = models.BooleanField(blank=True, null=True)
    comentarios_foto_infantil_bn_titulo_electronico = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Foto Infantil B/N')
    comentarios_foto_infantil_color_titulo_electronico = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Foto Infantil Color')
    comentarios_curp_titulo_electronico = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios CURP')
    comentarios_acta_nacimiento_titulo_electronico = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Acta de Nacimiento')
    comentarios_certificado_bachiller_titulo_electronico = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Certificado de Bachiller')
    comentarios_tsu_titulo_electronico = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios TSU')
    created_at_titulo_electronico = models.DateTimeField(auto_now_add=True)
    updated_at_titulo_electronico = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = 'ID_alumno: ' + str(self.id_alumno_titulo_electronico) + '\n'
        return fila
    def delete(self, using= None, keep_parents= False):
        self.foto_infantil_bn_titulo_electronico.storage.delete(self.foto_infantil_bn_titulo_electronico.name)
        self.foto_infantil_color_titulo_electronico.storage.delete(self.foto_infantil_color_titulo_electronico.name)
        self.curp_titulo_electronico.storage.delete(self.curp_titulo_electronico.name)
        self.acta_nacimiento_titulo_electronico.storage.delete(self.acta_nacimiento_titulo_electronico.name)
        self.certificado_bachiller_titulo_electronico.storage.delete(self.certificado_bachiller_titulo_electronico.name)
        self.tsu_titulo_electronico.storage.delete(self.tsu_titulo_electronico.name)
        super().delete()

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



    

    