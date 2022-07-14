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
    enrollment_student = models.CharField(primary_key=True, max_length=15)#matricula del estudiante
    id_user_student = models.ForeignKey(User, on_delete=models.CASCADE)#id del usuario del estudiante
    name_student = models.CharField(max_length=50)#nombre del estudiante
    last_name_student = models.CharField(max_length=50, default='')#apellido del estudiante
    second_last_name_student = models.CharField(max_length=50, default='')#segundo apellido del estudiante
    career_student = models.CharField(max_length=50)#carrera del estudiante
    area_career_student = models.CharField(max_length=50, default='')#area de la carrera del estudiante
    gender_student = models.CharField(max_length=50, default='')#genero del estudiante
    email_student = models.EmailField(max_length=50)#email
    phone_student = models.CharField(max_length=50)#tel
    created_at_student = models.DateTimeField(auto_now_add=True)
    updated_at_student = models.DateTimeField(auto_now=True)
    
    estadiasTSU_student = models.BooleanField(default=False)
    estadiasIngLic_student = models.BooleanField(default=False)

    def __str__(self):
        return self.enrollment_student + ' - ' + self.name_student 


class degreeCertificate(models.Model):
    id_degree_certificate = models.AutoField(primary_key=True)#id del certificado de grado
    enrollment_student_degree_id = models.ForeignKey(student, on_delete=models.CASCADE)#id del estudiante
    name_student_degree = models.CharField(max_length=50, default='')#nombre del estudiante
    last_name_degree = models.CharField(max_length=50, default='')
    second_last_name_degree = models.CharField(max_length=50, default='')
    syllabus_year_degree = models.IntegerField(default=0)#año de plan de estudios
    start_school_term_degree = models.CharField(max_length=50, default='')#inicioo del periodo escolar
    end_school_term_degree = models.CharField(max_length=50, default='')#fin del periodo escolar
    career_degree = models.CharField(max_length=50, default='')#carrera
    area_career_degree = models.CharField(max_length=50, default='')
    type_career_degree = models.CharField(max_length=50, default='')#tipo de carrera
    head_school_services_area_degree = models.CharField(max_length=50, default='')#encargado de area de servicios escolares
    director_career_degree = models.CharField(max_length=50, default='')
    ratings_degree = models.TextField(default='')#calificaciones

    created_at_degree = models.DateTimeField(auto_now_add=True)
    updated_at_degree = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = self.enrollment_student_degree_id + ' ' + self.name_student_degree
        return fila

idFileUser = uuid.uuid4()
class electronicDegree(models.Model):
    id_electronic_degree = models.AutoField(primary_key=True)#id del titulo electronico
    id_alumno_electronic_degree_id = models.ForeignKey(student, on_delete=models.CASCADE, default='')#id del estudiante
    small_photo_bw_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Foto Infantil B/N')
    small_photo_color_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Foto Infantil Color')
    curp_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='CURP')
    birth_certificate_electronic_degree =  models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Acta de Nacimiento')
    high_school_certificate_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='Certificado de Bachiller')
    tsu_electronic_degree = models.FileField(upload_to='filesT/'+str(idFileUser),  blank=True, verbose_name='TSU')
    status_small_photo_bw_electronic_degree = models.BooleanField(blank=True, null=True)
    status_small_photo_color_electronic_degree = models.BooleanField(blank=True, null=True)
    status_curp_electronic_degree = models.BooleanField(blank=True, null=True)
    status_birth_certificate_electronic_degree = models.BooleanField(blank=True, null=True)
    status_high_school_certificate_electronic_degree = models.BooleanField(blank=True, null=True)
    status_tsu_electronic_degree = models.BooleanField(blank=True, null=True)
    comments_small_photo_bw_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Foto Infantil B/N')
    comments_small_photo_color_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Foto Infantil Color')
    comments_curp_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios CURP')
    comments_birth_certificate_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Acta de Nacimiento')
    comments_high_school_certificate_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios Certificado de Bachiller')
    comments_tsu_electronic_degree = models.TextField(default='Sin comentarios', blank=True, verbose_name='Comentarios TSU')
    
    created_at_electronic_degree = models.DateTimeField(auto_now_add=True)
    updated_at_electronic_degree = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = 'ID_alumno: ' + str(self.id_alumno_titulo_electronico) + '\n'
        return fila
    
    
    
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



    

    