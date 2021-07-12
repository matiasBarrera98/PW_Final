from typing import ContextManager
from django.shortcuts import render, redirect
from .models import Animal, Mascota
from .forms import Agregamascota

# Create your views here.

def index (request):
    return render(request, 'sitioVet/index.html', {})

def clientes (request):
    return render(request, 'sitioVet/clientes.html', {})

def consultas (request):
    return render(request, 'sitioVet/consultas.html', {})

def contacto (request):
    return render(request, 'sitioVet/contacto.html', {})


def medicos (request):
    return render(request, 'sitioVet/medicos.html', {})


def pelu (request):
    return render(request, 'sitioVet/pelu.html', {})

def vacunacion(request):
    return render(request, 'sitioVet/vacunacion.html', {})

def nosotros(request):
    return render(request, 'sitioVet/nosotros.html', {})

def mascotas(request):
    info = Mascota.objects.all()
    contexto = {'mascotas' : info}
    return render (request, 'sitioVet/mascotas.html', context=contexto)

def crear(request):
    datos = {'form' : Agregamascota()} 
    if request.method == 'POST' : 
        formulario = Agregamascota(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos guardados correctamente'
        else :
            datos['mensaje'] = 'Datos ya guardados'
    return render(request, 'sitioVet/crear.html', context=datos)

def eliminar(request, id):
    mascota = Mascota.objects.get(idMascota=id)
    mascota.delete()
    return redirect(to="mascotas")
    
