from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def msg01(request):
	return HttpResponse("msg01")

def hoy(request):
	dia = datetime.now()
	texto = f"Hoy es {dia}"
	return HttpResponse(texto)

def param01(self, parametro01):
	textopara01 = f".<br><br>| {parametro01}"
	return HttpResponse(textopara01)
					 