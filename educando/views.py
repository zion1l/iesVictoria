from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from educando.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/usuarios/privado_admin/')

def ingresar(request):
    formulario = AuthForm()
    if request.method == 'POST':
        formulario = AuthForm(data=request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    perfil = Usuarios_Perfiles.objects.filter(id_usuario_id=acceso.id).values('id_perfil__perfil')
                    if len(perfil)>0:
                        if perfil[0]['id_perfil__perfil']== 'ADMINISTRADOR':
                            return HttpResponseRedirect('/usuarios/privado_admin')
                        elif perfil[0]['id_perfil__perfil']== 'PROFESOR':
                            return HttpResponseRedirect('/usuarios/privado_profesor')
                        elif perfil[0]['id_perfil__perfil']== 'ALUMNO':
                            return HttpResponseRedirect('/usuarios/privado_alumno')
                    else:
                        return render(request, 'educando/nopermisos.html')
                else:
                    return render(request, 'educando/noactivo.html')
            else:
                return render(request, 'educando/nousuario.html')
        else:
            messages.add_message(request, messages.ERROR, 'Usuario y contraseña no coinciden')
            return render(request, 'educando/ingresar.html', {'formulario': formulario})
    return render(request, 'educando/ingresar.html', {'formulario':formulario})

def agenda_base(request):
    usuario= request.user
    return render(request, 'educando/agenda_base.html', {'usuario':usuario})

def notas_alumnos(request):
    usuario= request.user
    return render(request, 'educando/notas_alumnos.html', {'usuario':usuario})

@login_required(login_url='educando/ingresar')
def privado_admin(request):
    formulario = UserCreationForm()
    usuario= request.user
    return render(request, 'educando/privado_admin.html', {'usuario':usuario, 'formulario':formulario})

@login_required(login_url='educando/ingresar')
def privado_alumno(request):
    usuario= request.user
    return render(request, 'educando/privado_alumno.html', {'usuario':usuario})

@login_required(login_url='educando/ingresar')
def privado_profesor(request):
    usuario= request.user
    return render(request, 'educando/privado_profesor.html', {'usuario':usuario})

