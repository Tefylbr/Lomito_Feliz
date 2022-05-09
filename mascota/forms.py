from cProfile import label
from pyexpat import model
from django.forms import *
from matplotlib import image
from .models import *


class Agregarmascota (ModelForm):
    class Meta:
        model = RegistroMascota 
        fields = [
            'nombre',
            'edad',
            'alimentacion',
            'fecha_de_rescate',
            'raza',
            'enfermedades',
            'imagen'
            ]
        labels = {
            'nombre':'Nombre',
            'edad': 'Edad',
            'alimentacion':'Alimentacion',
            'fecha_de_rescate':'Fecha de rescate',
            'raza': 'Raza',
            'enfermedades': 'Enfermedades',
            'imagen': 'Imagen',
        }
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'edad': TextInput(attrs={'class':'form-control'}),
            'alimentacion':TextInput(attrs={'class':'form-control'}),
            'fecha_de_rescate':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control','placeholder':'Fecha de rescate','type':'date'}),
            'raza': TextInput(attrs={'class':'form-control'}),
            'enfermedades': TextInput(attrs={'class':'form-control'}),
        }

class CambiarComida(ModelForm):
    class Meta:
        model = RegistroMascota
        fields = ['alimentacion']
        labels = {
            'alimentacion':''
        }
        widgets = {
            
        }