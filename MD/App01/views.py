from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse
from django.db import models
from .models import Destino
from .models import Presupuestar
from django import forms
from .forms import IngresarFormulario

# Create your views here.


def inicio(request):

    return render(request, "App01/inicio.html")


def busqueda(request):

    return render(request, "App01/busqueda.html")


def estado(request):

    return render(request, "App01/estado.html")


def ingrese(request):

    return render(request, "App01/ingrese.html")


def ofertas(request):
    ofertas = Destino.objects.all() 
    contexto = {"ofertas": ofertas} 
    return render(request, "App01/ofertas.html", contexto)


def formIngrese(request):
    print(request.POST)
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