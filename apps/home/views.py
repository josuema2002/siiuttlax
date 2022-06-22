# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps import config

#importar los modelos
from apps.home.models import alumno, empleado, certificadoTitulacion, tituloElectronico, estadisticasTitulacion
from django.contrib.auth.models import User

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
                html_template = loader.get_template('home/tituloElectronico/' + load_template)
            elif request.path.split('/')[-2] == 'certificado':
                html_template = loader.get_template('home/certificado/' + load_template)
            elif request.path.split('/')[-2] == 'folio':
                html_template = loader.get_template('home/folio/' + load_template)
            elif request.path.split('/')[-2] == 'fileUpload':
                #return HttpResponseRedirect('/soloAlumno') usar
                html_template = loader.get_template('home/fileUpload/' + load_template)
            else:
                html_template = loader.get_template('home/' + load_template)
        else:
            if request.path.split('/')[-2] == 'estadisticas':
                return HttpResponseRedirect('/404')
            elif request.path.split('/')[-2] == 'tituloElectronico':
                return HttpResponseRedirect('/404')
            elif request.path.split('/')[-2] == 'certificado':
                return HttpResponseRedirect('/404')
            elif request.path.split('/')[-2] == 'folio':
                return HttpResponseRedirect('/404')
            elif request.path.split('/')[-2] == 'fileUpload':
                #html_template = loader.get_template('home/fileUpload/' + load_template) usar
                return HttpResponseRedirect('/404')
            else:
                html_template = loader.get_template('home/' + load_template)


        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
