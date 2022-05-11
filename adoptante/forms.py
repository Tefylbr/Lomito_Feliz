from random import choices
from typing import List
from django.contrib.auth.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import *

estados={
        ('Solicitud enviada','Solicitud enviada'),
        ('En proceso','En proceso'),
        ('Solicitud aceptada','Solicitud aceptada'),
    }

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

class VerAdoptante (ModelForm):
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
            'NumeroMasc':'Cantidad de mascotas',
            'Razones':'Razones',
            'Estado':'Estado',
        }
        widgets = {
            'Nombre':TextInput(attrs={'readonly':'readonly'}),
            'Edad':TextInput(attrs={'readonly':'readonly'}),
            'Correo':TextInput(attrs={'readonly':'readonly'}),
            'Telefono':TextInput(attrs={'readonly':'readonly'}),
            'Domicilio':TextInput(attrs={'readonly':'readonly'}),
            'NumeroMasc':TextInput(attrs={'readonly':'readonly'}),
            'Razones':Textarea(attrs={'readonly':'readonly'}),
            'Estado': Select(choices= estados)
        }