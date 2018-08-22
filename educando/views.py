from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render(request,'educando/usuario.html', {'formulario':formulario})

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(request, 'educando/noactivo.html')
            else: return render(request, 'educando/nousuario.html')
    else: formulario = AuthenticationForm()
    return render(request, 'educando/ingresar.html', {'formulario':formulario})

@login_required(login_url='educando/ingresar')
def privado(request):
    usuario= request.user
    return render(request, 'educando/privado.html', {'usuario':usuario})