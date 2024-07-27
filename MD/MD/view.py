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

def Template01(self):
	categoria = "M" 
	tipo = "D" 
	listaPrecios = [8, 15, 100, 25, 500]
	dicci = {"c": categoria, "t": tipo, "h": datetime.now(), "pre": listaPrecios}
	miHtml = open("D:\_DOCUMENTOS\CODERHOUSE\Phyton\Entrega3\TerceraPreEntregaDiliberto\MD\MD\PLANTILLAS\Template01.html") 
	plantilla = Template(miHtml.read()) 
	miHtml.close() 
	miContexto = Context(dicci) 
	documento = plantilla.render(miContexto) 
	return HttpResponse(documento) 
					 