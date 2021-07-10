from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    return render(request, 'sitioVet/Paginainicial.html', {})

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

def vacunacion (request):
    return render(request, 'sitioVet/vacunacion.html', {})

def nosotros (request):
    return render(request, 'sitioVet/nosotros.html', {})
