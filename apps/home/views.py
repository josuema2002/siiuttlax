# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template


        if request.path.split('/')[-2] == 'estadisticas':
            html_template = loader.get_template('home/estadisticas/' + load_template)
        elif request.path.split('/')[-2] == 'tituloElectronico':
            html_template = loader.get_template('home/tituloElectronico/' + load_template)
        elif request.path.split('/')[-2] == 'certificado':
            html_template = loader.get_template('home/certificado/' + load_template)
        elif request.path.split('/')[-2] == 'folio':
            html_template = loader.get_template('home/folio/' + load_template)
        else:
            html_template = loader.get_template('home/' + load_template)


        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
