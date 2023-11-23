"""
URL configuration for proyecto_gaes5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from  . import views
from sesiones import views
from sesiones.forms import RegistrationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('login', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('agendar/', views.agendar, name='agendar'),
    path('index/', views.index, name='index'),
    path('indexr/', views.indexr, name='indexr'),
    path('Menu/', views.Menu, name='Menu'),
    path('menuAdmin/', views.menuAdmin, name='menuAdmin'),
    path('verAgenda/', views.verAgenda, name='verAgenda'),
    path('asignarR/', views.asignarR, name='asignarR'),
    path('contactos/', views.contactos, name='contactos'),
    path('crearCita/', views.crearCita, name='crearCita'),
    path('editarCita/', views.editarCita, name='editarCita'),
]
