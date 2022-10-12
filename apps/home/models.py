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

class student(models.Model):
    enrollment_student = models.CharField(primary_key=True, max_length=15, verbose_name="matricula")#matricula del estudiante
    id_user_student = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name="id user")#id del usuario del estudiante
    name_student = models.CharField(max_length=50, verbose_name="nombre")#nombre del estudiante
    last_name_student = models.CharField(max_length=50, default='', verbose_name="apellido paterno")#apellido del estudiante
    second_last_name_student = models.CharField(max_length=50, default='', verbose_name="apellido materno")#segundo apellido del estudiante
    career_student = models.CharField(max_length=50, verbose_name="carrera")#carrera del estudiante
    area_career_student = models.CharField(max_length=50, default='', null=True, verbose_name="area de la carrera")#area de la carrera del estudiante
    gender_student = models.CharField(max_length=50, default='', verbose_name="genero")#genero del estudiante
    email_student = models.EmailField(max_length=50, verbose_name="email")#email
    phone_student = models.CharField(max_length=50, verbose_name="tel")#tel
    created_at_student = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    updated_at_student = models.DateTimeField(auto_now=True, verbose_name="actualizado")
    
    estadiasTSU_student = models.BooleanField(default=False)
    estadiasIngLic_student = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.enrollment_student + ' ' + self.name_student
    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['enrollment_student']

class degreeCertificate(models.Model):
    id_degree_certificate = models.AutoField(primary_key=True, verbose_name="id del certificado")#id del certificado de grado
    enrollment_student_degree = models.ForeignKey(student, on_delete=models.CASCADE, default='', verbose_name="matricula del estudiante")#id del estudiante
    name_student_degree = models.CharField(max_length=50, default='', verbose_name="nombre")#nombre del estudiante
    last_name_degree = models.CharField(max_length=50, default='', verbose_name="apellido paterno")
    second_last_name_degree = models.CharField(max_length=50, default='', verbose_name="apellido materno")#segundo apellido del estudiante
    syllabus_year_degree = models.IntegerField(default=0, verbose_name="plan de estudios")#año de plan de estudios
    start_school_term_degree = models.CharField(max_length=50, default='', verbose_name="inicio del periodo escolar")#inicioo del periodo escolar
    end_school_term_degree = models.CharField(max_length=50, default='', verbose_name="fin del periodo escolar")#fin del periodo escolar
    career_degree = models.CharField(max_length=50, default='', verbose_name="carrera")#carrera
    area_career_degree = models.CharField(max_length=50, default='', verbose_name="area de la carrera")
    type_career_degree = models.CharField(max_length=50, default='', verbose_name="tipo de carrera")#tipo de carrera
    head_school_services_area_degree = models.CharField(max_length=50, default='', verbose_name="encargado de area de servicios escolares")#encargado de area de servicios escolares
    director_career_degree = models.CharField(max_length=50, default='', verbose_name="director de la carrera")
    ratings_degree = models.TextField(default='', verbose_name="calificaciones")#calificaciones

    created_at_degree = models.DateTimeField(auto_now_add=True, verbose_name="creado")
    updated_at_degree = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    def __str__(self):
        fila = self.enrollment_student_degree_id + ' ' + self.name_student_degree
        return fila
    class Meta:
        verbose_name = "Certificado de titulacion"
        verbose_name_plural = "Certificados de titulacion"

idFileUser = uuid.uuid4()
class electronicDegree(models.Model):
    id_electronic_degree = models.AutoField(primary_key=True, verbose_name="id del titulo")#id del titulo electronico
    id_student_electronic_degree = models.ForeignKey(student, on_delete=models.CASCADE, default='', verbose_name="matricula del estudiante")#id del estudiante
    small_photo_bw_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Foto Infantil B/N')
    small_photo_color_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Foto Infantil Color')
    curp_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='CURP')
    birth_certificate_electronic_degree =  models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Acta de Nacimiento')
    high_school_certificate_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Certificado de Bachiller')
    tsu_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='TSU')
    status_small_photo_bw_electronic_degree = models.BooleanField(blank=True, null=True, verbose_name="estatus de la foto b/n")
    status_small_photo_color_electronic_degree = models.BooleanField(blank=True, null=True, verbose_name="estatus de la foto a color")
    status_curp_electronic_degree = models.BooleanField(blank=True, null=True, verbose_name="estatus del curp")
    status_birth_certificate_electronic_degree = models.BooleanField(blank=True, null=True, verbose_name="estatus del acta de nacimiento")
    status_high_school_certificate_electronic_degree = models.BooleanField(blank=True, null=True, verbose_name="estatus del certificado de bachiller")
    status_tsu_electronic_degree = models.BooleanField(blank=True, null=True, verbose_name="estatus del certificado del TSU")
    comments_small_photo_bw_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Foto Infantil B/N')
    comments_small_photo_color_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Foto Infantil Color')
    comments_curp_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios CURP')
    comments_birth_certificate_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Acta de Nacimiento')
    comments_high_school_certificate_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Certificado de Bachiller')
    comments_tsu_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios TSU')
    
    created_at_electronic_degree = models.DateTimeField(auto_now_add=True)
    updated_at_electronic_degree = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = self.id_student_electronic_degree
        return fila

    def delete(self, *args, **kwargs):
        self.small_photo_bw_electronic_degree.delete()
        self.small_photo_color_electronic_degree.delete()
        self.curp_electronic_degree.delete()
        self.birth_certificate_electronic_degree.delete()
        self.high_school_certificate_electronic_degree.delete()
        self.tsu_electronic_degree.delete()
        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = "Titulo electronico"
        verbose_name_plural = "Titulos electronico"
    
# class estadisticasTitulacion(models.Model):
    # id_estadisticas_titulacion = models.AutoField(primary_key=True)
    # genero_estadisticas_titulacion = models.CharField(max_length=50)
    # ingreso_estadisticas_titulacion = models.IntegerField()
    # egreso_estadisticas_titulacion = models.IntegerField()
    # rezagados_estadisticas_titulacion = models.IntegerField()
    # total_estudiantes_estadisticas_titulacion = models.IntegerField()
    # total_titulados_estadisticas_titulacion = models.IntegerField()
    # total_no_titulados_estadisticas_titulacion = models.IntegerField()
    # created_at_estadisticas_titulacion = models.DateTimeField(auto_now_add=True)



    

    