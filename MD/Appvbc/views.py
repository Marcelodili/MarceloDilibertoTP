from django.shortcuts import render
# <clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# clases basadas en vistas>
from App01.models import Destino
from django.urls import reverse_lazy

class ofertasListView(ListView):
    model = Destino
    context_object_name = "ofertas"
    template_name = "Appvbc/ofertas.html"
# clases basadas en vistas>
