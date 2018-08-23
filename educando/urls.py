from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^ingresar/$',views.ingresar, name='ingresar'),
    url(r'^privado_admin/$',views.privado_admin, name='privado_admin'),
]