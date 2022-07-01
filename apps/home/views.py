# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from asyncio.windows_events import NULL
from codecs import register
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse

from apps import config

#importar los modelos
from apps.home.models import alumno, empleado, certificadoTitulacion, tituloElectronico, estadisticasTitulacion
from django.contrib.auth.models import User

#importar los forms
from apps.home.forms import fileUploadForm


PATHPROJECT = config.PATHPROJECT

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
            # obtener los datos de alumnos
            alumnos = alumno.objects.all()
            request.alumnos = alumnos

            if request.path.split('/')[-2] == 'estadisticas':
                html_template = loader.get_template('home/estadisticas/' + load_template)
            elif request.path.split('/')[-2] == 'tituloElectronico':

                i = 0
                for alumnoD in alumnos:
                    i += 1
                    # obtener los documentos recibidos
                    try:
                        tituloED = tituloElectronico.objects.get(id_alumno_titulo_electronico_id=str(alumnoD.matricula_alumno))
                        count = 0
                        if tituloED.acta_nacimiento_titulo_electronico:
                            count += 1
                        if tituloED.certificado_bachiller_titulo_electronico:
                            count += 1
                        if tituloED.curp_titulo_electronico:
                            count += 1
                        if tituloED.foto_infantil_bn_titulo_electronico:
                            count += 1
                        if tituloED.foto_infantil_color_titulo_electronico:
                            count += 1
                        if tituloED.tsu_titulo_electronico:
                            count += 1
                        request.alumnos[i-1].dr = count
                    except:
                        request.alumnos[i-1].dr = 0
                    
                    # obtener los documentos aceptados
                    try:
                        tituloED = tituloElectronico.objects.get(id_alumno_titulo_electronico_id=str(alumnoD.matricula_alumno))
                        count = 0
                        if tituloED.status_acta_nacimiento_titulo_electronico:
                            count += 1
                        if tituloED.status_certificado_bachiller_titulo_electronico:
                            count += 1
                        if tituloED.status_curp_titulo_electronico:
                            count += 1
                        if tituloED.status_foto_infantil_bn_titulo_electronico:
                            count += 1
                        if tituloED.status_foto_infantil_color_titulo_electronico:
                            count += 1
                        if tituloED.status_tsu_titulo_electronico:
                            count += 1
                        request.alumnos[i-1].da = count
                        if alumnoD.estadiasIngLic_alumno:
                            request.alumnos[i-1].dporcentage = int((count * 100) / 6)
                        else:
                            request.alumnos[i-1].dporcentage = int((count * 100) / 5)
                    except:
                        request.alumnos[i-1].da = 0
                        request.alumnos[i-1].dporcentage = int((0 * 100) / 6)

                    # obtener los documentos pendientes
                    try:
                        tituloED = tituloElectronico.objects.get(id_alumno_titulo_electronico_id=str(alumnoD.matricula_alumno))
                        count = 0
                        if tituloED.status_acta_nacimiento_titulo_electronico == None:
                            count += 1
                        if tituloED.status_certificado_bachiller_titulo_electronico == None:
                            count += 1
                        if tituloED.status_curp_titulo_electronico == None:
                            count += 1
                        if tituloED.status_foto_infantil_bn_titulo_electronico == None:
                            count += 1
                        if tituloED.status_foto_infantil_color_titulo_electronico == None:
                            count += 1
                        if tituloED.status_tsu_titulo_electronico == None:
                            count += 1
                        request.alumnos[i-1].dp = count
                    except:
                        request.alumnos[i-1].dp = 'Todos'

                
                if load_template == 'titulo-form.html':
                    try:
                        files = tituloElectronico.objects.get(id_alumno_titulo_electronico_id=str(request.GET['matricula']))
                        request.files = files
                        dataA = alumno.objects.get(matricula_alumno=str(request.GET['matricula']))
                        request.dataA = dataA
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

                html_template = loader.get_template('home/tituloElectronico/' + load_template)
            elif request.path.split('/')[-2] == 'certificado':
                
                #     form = FormularioCertificado(request.POST)
                #     if form.is_valid():
                #         plan_estudios = form.cleaned_data['plan_estudios']
                #         periodo_escolar_init = form.cleaned_data['periodo_escolar_init']
                #         periodo_escolar_end = form.cleaned_data['periodo_escolar_end']
                # else:
                #     form = FormularioCertificado()
                # request.form = form
                html_template = loader.get_template('home/certificado/' + load_template)
            elif request.path.split('/')[-2] == 'folio':
                html_template = loader.get_template('home/folio/' + load_template)
            elif request.path.split('/')[-2] == 'fileUpload':
                #return HttpResponseRedirect('/soloAlumno') usar
                html_template = loader.get_template('home/fileUpload/' + load_template)

                
                # peticiones de ajax
            elif request.path.split('/')[-2] == 'alumno':
                #obtener los datos POST de alumnos
                if request.method == 'POST':
                    #obtener los datos POST
                    datos = request.POST
                    #obtener la matricula
                    matricula = datos['matricula']
                    #obtener los datos del alumno con la matricula
                    alumnoOnli = alumno.objects.get(matricula=matricula)
                    return JsonResponse({"alumnoOnli":alumnoOnli}, status=200)
                else :
                    return HttpResponseRedirect('/404')


                # default
            else:
                html_template = loader.get_template('home/' + load_template)
        else:
            dataA = alumno.objects.get(id_user_alumno_id=str(request.user.id))
            matricula_alumno = dataA.matricula_alumno
            request.dataA = dataA

            if request.path.split('/')[-2] == 'estadisticas' or request.path.split('/')[-2] == 'tituloElectronico' or request.path.split('/')[-2] == 'certificado' or request.path.split('/')[-2] == 'folio':
                return HttpResponseRedirect('/404')
            elif request.path.split('/')[-2] == 'fileUpload':
                
                request.titleFormTituloElectronico = 'Subir'
                try:
                    files = tituloElectronico.objects.get(id_alumno_titulo_electronico_id=str(matricula_alumno))
                    request.files = files
                    request.titleFormTituloElectronico = 'Editar'
                except tituloElectronico.DoesNotExist:
                    pass

                if load_template == 'file-formF.html':
                    request.form = fileUploadForm(request.POST or None, request.FILES or None)
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

    # except template.TemplateDoesNotExist:

    #     html_template = loader.get_template('home/page-404.html')
    #     return HttpResponse(html_template.render(context, request))

    except Exception as e:
        request.error = e
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
