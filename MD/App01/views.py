from django.shortcuts import render
from django.urls import path, include


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

    return render(request, "App01/ofertas.html")
