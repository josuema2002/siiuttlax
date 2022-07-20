# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('titulacion', views.index, name='home'),
    re_path(r'^.*\.html', views.pages, name='pages'), #ver si existe una pagina con .html
    re_path(r'^.[0-9a-zA-Z_/-]*$', views.pages, name='pages'), #ver si existe una pagina sin extension (carpeta)
    
]

