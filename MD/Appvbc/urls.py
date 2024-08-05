from django.urls import path, include
from Appvbc import views

# http://127.0.0.1:8000/vbc/ofertas/listar
urlpatterns = [
    path("ofertas/listar", views.ofertasListView.as_view(), name="Ofertas.")
]