from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def msg01(request):
	return HttpResponse("msg01")
					 