# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from asyncio.windows_events import NULL
from codecs import register
from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render as render_template
from django.template import loader
from django.urls import reverse
from requests import request

from apps import config

#importar los modelos
from apps.home.models import student, degreeCertificate, electronicDegree, estadisticasTitulacion
from django.contrib.auth.models import User

#importar los forms
from apps.home.forms import fileUploadForm, certificadoTitulacionForm


PATHPROJECT = config.PATHPROJECT

@login_required(login_url="/login/")
def page_not_found_view(request, exception):
    return render_template(request, 'home/page-404.html', status=404)
    
@login_required(login_url="/login/")
def error500(request):
    return render_template(request, 'home/page-500.html', status=500)

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    request.PATHPROJECT = PATHPROJECT

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}

    request.PATHPROJECT = PATHPROJECT
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        if request.user.is_superuser:          
            try:
                certificados = degreeCertificate.objects.all()
                request.certificados = certificados
                alumnos = student.objects.all()
                request.alumnos = alumnos
                request.numCertificados = 0
                for certificado in certificados:
                    if str(certificado.__dict__['updated_at_degree']).split('-')[0] == str(datetime.now().year):
                        request.numCertificados += 1

                titulosElectronicos = electronicDegree.objects.all()
                request.titulosElectronicos = titulosElectronicos
                request.numTitulosElectronicos = 0
                if len(str(datetime.now().month)) == 1:
                    mes = '0' + str(datetime.now().month)
                else:
                    mes = str(datetime.now().month)
                for tituloElectronico in titulosElectronicos:
                    if str(str(tituloElectronico.__dict__['updated_at_electronic_degree'])).split('-')[1] == mes:
                        if tituloElectronico.birth_certificate_electronic_degree and tituloElectronico.high_school_certificate_electronic_degree and tituloElectronico.curp_electronic_degree and tituloElectronico.small_photo_bw_electronic_degree and tituloElectronico.small_photo_color_electronic_degree:
                            request.numTitulosElectronicos += 1
                        
            except:
                request.certificados = None
                request.alumnos = None
                request.numCertificados = 0
                request.numTitulosElectronicos = 0

            if request.path.split('/')[-2] == 'estadisticas':

                if load_template == 'charts-form.html':
                    1+1

                html_template = loader.get_template('home/estadisticas/' + load_template)
            elif request.path.split('/')[-2] == 'tituloElectronico':

                i = 0
                for alumnoD in alumnos:
                    i += 1
                    # obtener los documentos recibidos
                    try:
                        tituloED = electronicDegree.objects.get(id_student_electronic_degree=str(alumnoD.enrollment_student))
                        count = 0
                        if tituloED.birth_certificate_electronic_degree:
                            count += 1
                        if tituloED.high_school_certificate_electronic_degree:
                            count += 1
                        if tituloED.curp_electronic_degree:
                            count += 1
                        if tituloED.small_photo_bw_electronic_degree:
                            count += 1
                        if tituloED.small_photo_color_electronic_degree:
                            count += 1
                        if tituloED.tsu_electronic_degree:
                            count += 1
                        request.alumnos[i-1].dr = count
                    except Exception as e:
                        print(e)
                        request.alumnos[i-1].dr = 0
                    
                    # obtener los documentos aceptados
                    try:
                        tituloED = electronicDegree.objects.get(id_student_electronic_degree=str(alumnoD.enrollment_student))
                        count = 0
                        if tituloED.status_birth_certificate_electronic_degree:
                            count += 1
                        if tituloED.status_high_school_certificate_electronic_degree:
                            count += 1
                        if tituloED.status_curp_electronic_degree:
                            count += 1
                        if tituloED.status_small_photo_bw_electronic_degree:
                            count += 1
                        if tituloED.status_small_photo_color_electronic_degree:
                            count += 1
                        if tituloED.status_tsu_electronic_degree:
                            count += 1
                        request.alumnos[i-1].da = count
                        if alumnoD.estadiasIngLic_student:
                            request.alumnos[i-1].dporcentage = int((count * 100) / 6)
                        else:
                            request.alumnos[i-1].dporcentage = int((count * 100) / 5)
                    except:
                        request.alumnos[i-1].da = 0
                        request.alumnos[i-1].dporcentage = int((0 * 100) / 6)

                    # obtener los documentos pendientes
                    try:
                        tituloED = electronicDegree.objects.get(id_student_electronic_degree=str(alumnoD.enrollment_student))
                        count = 0
                        if tituloED.status_birth_certificate_electronic_degree == None:
                            count += 1
                        if tituloED.status_high_school_certificate_electronic_degree == None:
                            count += 1
                        if tituloED.status_curp_electronic_degree == None:
                            count += 1
                        if tituloED.status_small_photo_bw_electronic_degree == None:
                            count += 1
                        if tituloED.status_small_photo_color_electronic_degree == None:
                            count += 1
                        if alumnoD.estadiasIngLic_student:
                            if tituloED.status_tsu_electronic_degree == None:
                                count += 1
                        request.alumnos[i-1].dp = count
                    except:
                        request.alumnos[i-1].dp = 'Todos'

                
                if load_template == 'titulo-form.html':
                    try:
                        files = electronicDegree.objects.get(id_student_electronic_degree=str(request.GET['matricula']))
                        request.files = files
                        dataA = student.objects.get(enrollment_student=str(request.GET['matricula']))
                        request.dataA = dataA

                        request.form = fileUploadForm(request.POST or None, instance=files)
                        if request.method == 'POST':
                            if request.form.is_valid():
                                form = request.form
                                form.save()
                                return HttpResponseRedirect(PATHPROJECT+'/tituloElectronico/titulo-allT.html')
                            else:
                                return HttpResponse(request.form.errors.as_json())
                    except:
                        load_template = 'titulo-allT.html'

                if load_template == 'delete':
                    try:
                        matricula = request.GET['matricula']
                        dataTitulo = electronicDegree.objects.get(id_student_electronic_degree=matricula)
                        dataTitulo.delete()
                        return HttpResponseRedirect(PATHPROJECT+'/tituloElectronico/titulo-allT.html')
                    except:
                        return HttpResponseRedirect(PATHPROJECT+'/tituloElectronico/titulo-form.html?matricula='+request.GET['matricula'])

                html_template = loader.get_template('home/tituloElectronico/' + load_template)
            elif request.path.split('/')[-2] == 'certificado':

                
                
                if load_template == 'certificado-form.html':
                    request.form = certificadoTitulacionForm(request.POST or None)
                    if request.method == 'POST' and request.is_ajax():
                        if request.form.is_valid():
                            form = request.form
                            form.save()
                            return JsonResponse({'status': '201', 'message': 'Certificado guardado'})
                        else:
                            return HttpResponse(request.POST)

                if load_template == 'certificado-formE.html':
                    try:
                        matricula = request.GET['matricula']
                        dataAlumno = degreeCertificate.objects.get(enrollment_student_degree=matricula)
                        request.form = certificadoTitulacionForm(request.POST or None, instance=dataAlumno)
                        request.dataAlumno = dataAlumno
                        if request.method == 'POST' and request.is_ajax():
                            if request.form.is_valid():
                                form = request.form
                                form.save()
                                return JsonResponse({'status': '201', 'message': 'Certificado guardado'})
                            else:
                                return HttpResponse(request.POST)
                    except:
                        return HttpResponseRedirect(PATHPROJECT+'/certificado/certificado-allC.html')
                    
                if load_template == 'delete':
                    try:
                        matricula = request.GET['matricula']
                        dataAlumno = degreeCertificate.objects.get(enrollment_student_degree=matricula)
                        dataAlumno.delete()
                        return HttpResponseRedirect(PATHPROJECT+'/certificado/certificado-allC.html')
                    except:
                        return HttpResponseRedirect(PATHPROJECT+'/certificado/certificado-allC.html')

                html_template = loader.get_template('home/certificado/' + load_template)
            elif request.path.split('/')[-2] == 'folio':
                html_template = loader.get_template('home/folio/' + load_template)
            elif request.path.split('/')[-2] == 'fileUpload':
                #return HttpResponseRedirect('/soloAlumno') usar
                html_template = loader.get_template('home/fileUpload/' + load_template)

                
                # peticiones de ajax externas
            elif request.path.split('/')[-1] == 'alumno1':
                # obtener los datos POST de alumnos
                if request.method == 'POST' and request.is_ajax():
                    #obtener los datos POST
                    datos = request.POST
                    #obtener la matricula
                    matricula = datos['matricula']
                    #obtener los datos del alumno con la matricula
                    alumnoOnli = student.objects.get(enrollment_student=matricula)
                    return JsonResponse({
                        'enrollment_student_degree': alumnoOnli.enrollment_student, 
                        'name_student_degree': alumnoOnli.name_student, 
                        'last_name_degree': alumnoOnli.last_name_student, 
                        'second_last_name_degree': alumnoOnli.second_last_name_student,
                        'syllabus_year_degree': 2020,
                        'start_school_term_degree': '01/2022',
                        'end_school_term_degree': '01/2022',
                        'career_degree': 'Administracion',
                        'area_career_degree': 'Recursos Humanos',
                        'type_career_degree': 'Tecnico Superior Universitario',
                        'head_school_services_area_degree': 'Arq. Alfredo Ajuria Huerta',
                        'director_career_degree': 'M. en C. Yesenia Ricón Enríquez',
                        'ratings_degree': '[{"materia": "Matematicas", "horas": 50,"calificacion": 10},{"materia": "Español", "horas": 100, "calificacion": 9},{"materia": "Historia", "horas": 79, "calificacion": 8}]'
                    })
                else :
                    return HttpResponseRedirect('/404/')


                # default
            else:
                html_template = loader.get_template('home/' + load_template)
        else:
            dataA = student.objects.get(id_user_student=str(request.user.id))
            enrollment_student = dataA.enrollment_student
            request.dataA = dataA

            request.titleFormTituloElectronico = 'Subir'
            try:
                files = electronicDegree.objects.get(id_student_electronic_degree=str(enrollment_student))
                request.files = files
                request.titleFormTituloElectronico = 'Editar'
            except electronicDegree.DoesNotExist:
                request.titleFormTituloElectronico = 'Subir'

            if request.path.split('/')[-2] == 'estadisticas' or request.path.split('/')[-2] == 'tituloElectronico' or request.path.split('/')[-2] == 'certificado' or request.path.split('/')[-2] == 'folio':
                return HttpResponseRedirect('/404')
            elif request.path.split('/')[-2] == 'fileUpload':
                

                if load_template == 'file-formF.html':
                    if request.titleFormTituloElectronico == 'Subir':
                        request.form = fileUploadForm(request.POST or None, request.FILES or None)
                    else:
                        request.form = fileUploadForm(request.POST or None, request.FILES or None, instance=files)
                    if request.method == 'POST':
                        if request.form.is_valid():
                            form = request.form
                            form.save()
                            return HttpResponseRedirect(PATHPROJECT+'/fileUpload/file-allF.html')
                        else:
                            return HttpResponse(request.form.errors.as_json())

                html_template = loader.get_template('home/fileUpload/' + load_template)
            else:
                html_template = loader.get_template('home/' + load_template)

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        request.error = e
        try:
            if e.errno == 13:
                html_template = loader.get_template('home/page-404.html')
                return HttpResponse(html_template.render(context, request))
        except:
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))
