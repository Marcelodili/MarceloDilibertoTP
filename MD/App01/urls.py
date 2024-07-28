from django.urls import path
from App01 import views
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
]

