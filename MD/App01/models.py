from django.db import models

# Create your models here.


class Cliente(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    credito = models.IntegerField()
    rubro = models.IntegerField()
    email = models.EmailField()
    fechanacimiento = models.DateField() 


class Transporte(models.Model): 
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=30) 
    descripcion = models.CharField(max_length=30) 
    empresa = models.CharField(max_length=30)
    precio = models.IntegerField()

class Destino(models.Model):
    codigo = models.IntegerField()	 
    nombre = models.CharField(max_length=30) 
    ubicacion = models.CharField(max_length=30) 
    contacto = models.EmailField() 
    hotel = models.CharField(max_length=30) 
    precio = models.IntegerField()

class Presupuestar(models.Model):
    codigo = models.IntegerField()	 
    clientedni = models.IntegerField()
    codigotransporte = models.IntegerField()
    codigodestino = models.IntegerField()
    comentario = models.CharField(max_length=30) 
    fechaviaje = models.DateField()
    dias = models.IntegerField()
    pasajeros = models.IntegerField() 
    potencial = models.BooleanField()
    enviado = models.DateField()
