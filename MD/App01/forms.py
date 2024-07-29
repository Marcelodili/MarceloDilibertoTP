from django import forms


class IngresarFormulario(forms.Form):
    clientedni = forms.IntegerField()
    codigotransporte = forms.IntegerField()
    codigodestino = forms.IntegerField()
    comentario = forms.CharField(max_length=30)
    fechaviaje = forms.DateField()
    dias = forms.IntegerField()
    pasajeros = forms.IntegerField()