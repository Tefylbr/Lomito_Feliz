from django.contrib.auth.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import *



class SolicitudAdopcion (ModelForm):
    class Meta:
        model = SolicitudAdop 
        fields = [
            'Nombre',
            'Edad',
            'Correo',
            'Telefono',
            'Domicilio',
            'NumeroMasc',
            'Razones',
            'Estado',
            ]
        labels = {
            'Nombre':'Nombre',
            'Edad':'Edad',
            'Correo':'Correo',
            'Telefono':'Telefono',
            'Domicilio':'Domicilio',
            'NumeroMasc':'NumeroMasc',
            'Razones':'Razones',
            'Estado':'Estado',
        }
        widgets = {
            'Estado':TextInput(attrs={'readonly':'readonly'})
        }