# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import student, degreeCertificate, electronicDegree
# Register your models here.

admin.site.register(student)
admin.site.register(degreeCertificate)
admin.site.register(electronicDegree)

