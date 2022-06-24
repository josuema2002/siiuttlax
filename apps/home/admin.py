# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import alumno, empleado, certificadoTitulacion, tituloElectronico, estadisticasTitulacion
# Register your models here.

admin.site.register(alumno)
admin.site.register(empleado)
admin.site.register(certificadoTitulacion)
admin.site.register(tituloElectronico)
admin.site.register(estadisticasTitulacion)

