from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^ingresar/$',views.ingresar, name='ingresar'),
    url(r'^privado_admin/$',views.privado_admin, name='privado_admin'),
    url(r'^privado_alumno/$',views.privado_alumno, name='privado_alumno'),
    url(r'^privado_profesor/$',views.privado_profesor, name='privado_profesor'),
    url(r'^agenda_base/$',views.agenda_base, name='agenda_base'),
    url(r'^notas_alumnos/$', views.notas_alumnos, name='notas_alumnos'),
]