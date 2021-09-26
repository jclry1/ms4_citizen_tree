"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler403, handler404, handler500
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings



urlpatterns = [
    # Django
    path('adm-cit-tree/', admin.site.urls), #Changed for admin-hardening

    # Favicon - from https://simpleit.rocks/python/django/django-favicon-adding/
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    
    # MS4
    path('', include('home.urls')),    
    path('accounts/', include('allauth.urls')),
    path('calculator/', include('calculator.urls')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('donations/', include ('donations.urls', namespace='donations')),
]

handler404 = 'home.views.custom_error_404'
handler403 = 'home.views.custom_error_403'
handler500 = 'home.views.custom_error_500'

