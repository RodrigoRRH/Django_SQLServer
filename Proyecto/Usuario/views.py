from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.


def home(request):
    ListaUsuarios = Usuario.objects.all()
    messages.success(request, '¡Usuarios listados!')
    return render(request, "gestionUsuarios.html", {"usuarios":ListaUsuarios})

def registrarUsuario(request):
    dni = request.POST['numDNI']
    nombres = request.POST['txtNombres']
    apellidos = request.POST['txtApellidos']
    contraseña = request.POST['txtContraseña']

    usuario = Usuario.objects.create(dni=dni, nombres=nombres, apellidos=apellidos, contraseña=contraseña)
    messages.success(request, '¡Usuario registrado!')
    return redirect('/')

def edicionUsuario(request, dni):
    usuario = Usuario.objects.get(dni=dni)
    return render(request, "edicionUsuario.html", {"usuario":usuario})

def editarUsuario(request):
    dni = request.POST['numDNI']
    nombres = request.POST['txtNombres']
    apellidos = request.POST['txtApellidos']
    contraseña = request.POST['txtContraseña']

    usuario = Usuario.objects.get(dni=dni)
    usuario.nombres = nombres
    usuario.apellidos = apellidos
    usuario.contraseña = contraseña
    usuario.save()

    messages.success(request, '¡Usuario actualizado!')

    return redirect('/')



def eliminarUsuario(request, dni):
    usuario = Usuario.objects.get(dni=dni)
    usuario.delete()

    messages.success(request, '¡Usuario eliminado!')

    return redirect('/')
