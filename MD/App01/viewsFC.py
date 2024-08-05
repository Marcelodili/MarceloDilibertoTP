from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse
from django.db import models
from .models import Destino
from .models import Presupuestar
from .models import Cliente
from .models import Transporte
from django import forms
from .forms import IngresarFormulario
from .forms import IngresarFormularioCliente
from .forms import BuscaPresuForm

# # Create your views here.


def inicio(request):

    return render(request, "App01/inicio.html")


def busqueda(request):

    return render(request, "App01/busqueda.html")


def ofertas(request):
    ofertas = Destino.objects.all() 
    contexto = {"ofertas": ofertas} 
    return render(request, "App01/ofertas.html", contexto)


def ofertast(request):
    ofertast = Transporte.objects.all()
    contexto = {"ofertast": ofertast} 
    return render(request, "App01/ofertast.html", contexto)


def ingrese(request):
    if request.method == "POST":
        mi_formulario = IngresarFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            ingrese = Presupuestar(clientedni=informacion["clientedni"], codigotransporte=informacion["codigotransporte"], codigodestino=informacion["codigodestino"], comentario=informacion["comentario"], fechaviaje=informacion["fechaviaje"], dias=informacion["dias"], pasajeros=informacion["pasajeros"])
            ingrese.save()
            return render(request, "App01/inicio.html")
    else:
        mi_formulario = IngresarFormulario()
    return render(request, "App01/ingrese.html", {"mi_formulario": mi_formulario})


def ingresecliente(request):
    if request.method == "POST":
        mi_formulario = IngresarFormularioCliente(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            ingrese = Cliente(dni=informacion["dni"], nombre=informacion["nombre"], email=informacion["email"], fechanacimiento=informacion["fechanacimiento"])
            ingrese.save()
            return render(request, "App01/inicio.html")
    else:
        mi_formulario = IngresarFormularioCliente()
    return render(request, "App01/ingresecliente.html", {"mi_formulario": mi_formulario})

def ingrese_input(request):
    if request.method == "POST":
        ingrese = Presupuestar(clientedni=request.POST["clientedni"], codigotransporte=request.POST["codigotransporte"], codigodestino=request.POST["codigodestino"], comentario=request.POST["comentario"], fechaviaje=request.POST["fechaviaje"], dias=request.POST["dias"], pasajeros=request.POST["pasajeros"])
#        print(request.POST)
#        print(f"\n\n))"
        ingrese.save()
        return render(request, "App01/inicio.html")
    return render(request, "App01/ingrese.html")


def buscapresupuestoG(request):
    return render(request, "App01/buscapresupuestoG.html")

def buscar(request):
    if request.GET["clientedni"]:

        clientedni = request.GET["clientedni"]
        info = Presupuestar.objects.filter(clientedni=clientedni)
        return render(request, "App01/buscar.html", {"Presupuestado": clientedni})
    else:
        respuesta = "sin datos"
    HttpResponse(respuesta)

def buscapresupuesto(request):
    if request.method == "POST":
        mi_formulario = BuscaPresuForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
#            ingrese = Presupuestar.objects.filter(clientedni__icontains=informacion["clientedni"])
            ingrese = Presupuestar.objects.filter(clientedni=informacion["clientedni"])
            return render(request, "App01/buscap.html", {"Presupuestos": ingrese})
    else:
        mi_formulario = BuscaPresuForm()
    return render(request, "App01/buscapresupuesto.html", {"mi_formulario": mi_formulario})






