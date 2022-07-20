# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path  # add this

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from django.conf.urls import handler404
from django.conf.urls import handler500
from apps.home import views


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route

    path('titulacion/', include('apps.home.urls')),

    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.page_not_found_view
handler500 = views.error500


print("MEDIA_URL"+settings.MEDIA_URL)
print("MEDIA_ROOT"+settings.MEDIA_ROOT)