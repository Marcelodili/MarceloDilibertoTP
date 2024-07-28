from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from App01.models import Transporte


def msg01(request):
	return HttpResponse("msg01")


def hoy(request):
	dia = datetime.now()
	texto = f"Hoy es {dia}"
	return HttpResponse(texto)


def param01(self, parametro01):
	textopara01 = f".<br><br>| {parametro01}"
	return HttpResponse(textopara01)


def Template01(self):
	categoria = "M" 
	tipo = "D" 
	listaPrecios = [8, 15, 100, 25, 500]
	dicci = {"c": categoria, "t": tipo, "h": datetime.now(), "pre": listaPrecios}
	plantilla = loader.get_template("Template01.html")
	documento = plantilla.render(dicci) 
	return HttpResponse(documento) 


def transportes(self):
	transporte = Transporte(codigo=1, nombre="Avion", empresa="Aerolínea")
	transporte.save()
	texto = f"nombre {transporte.nombre} camada {transporte.codigo}"
	transporte = Transporte(codigo=2, nombre="Micro", empresa="Bus")
	transporte.save()
	texto += f"nombre {transporte.nombre} camada {transporte.codigo}"
	return HttpResponse(texto)
