from django import forms


class IngresarFormulario(forms.Form):
    clientedni = forms.IntegerField()
    codigotransporte = forms.IntegerField()
    codigodestino = forms.IntegerField()
    comentario = forms.CharField(max_length=30, required=False)
    fechaviaje = forms.DateField()
    dias = forms.IntegerField()
    pasajeros = forms.IntegerField()


class IngresarFormularioCliente(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    fechanacimiento = forms.DateField()
 

class BuscaPresuForm(forms.Form):
    clientedni = forms.IntegerField()
