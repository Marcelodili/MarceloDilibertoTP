from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse
from django.db import models
from .models import Destino



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