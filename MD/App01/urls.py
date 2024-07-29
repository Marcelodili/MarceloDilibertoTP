from django.urls import path
from App01 import views
from .views import inicio
from App01.views import busqueda
from App01.views import estado
from App01.views import ingrese
from App01.views import ofertas
from MD.view import msg01
from MD.view import hoy
from MD.view import param01
from MD.view import Template01


urlpatterns = [
    # inicio
    #  destinos y transportes/ busqueda de destinos / ingreso consulta / estado consulta 
    path('MD01/', msg01),
    path('MD02/', hoy),
    path('MD03/<parametro01>', param01),
    path('MD04/', Template01),
#    path("", inicio),
#    path("busqueda", busqueda),
#    path("estado", estado),
#    path("ingrese", ingrese),
#    path("ofertas", ofertas),
    path('', views.inicio, name="Inicio"),
    path('busqueda/', views.busqueda, name="Busqueda"), 
    path('estado/', views.estado, name="Estado"), 
    path('ingrese/', views.ingrese, name="Ingrese"), 
    path('ofertas/', views.ofertas, name="Ofertas"), 
]

