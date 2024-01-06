"""
URL configuration for foreverfinds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPage, name='index'),
    path('living/', views.LivingPage, name='living'),
    path('kitchen_dining/', views.Kitchen_DiningPage, name='kitchen_dining'),
    path('bedroom/', views.BedroomPage, name='bedroom'),
    path('contact/', views.ContactPage, name='contact'),
    path('homeoffice/', views.HomeOfficePage, name='homeoffice'),
    path('Outdoor/', views.OutdoorPage, name='Outdoor')
]

urlpatterns += staticfiles_urlpatterns()   

