from cProfile import label
from pyexpat import model
from click import option
from django.forms import *
from matplotlib import image
from .models import *

Vacunas={
        ('Parvovirus y moquillo','Parvovirus y moquillo'),
        ('Polivalente','Polivalente'),
        ('Contra la rabia','Contra la rabia'),
    }
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
            'imagen',
            'vacunacion',
            ]
        labels = {
            'nombre':'Nombre',
            'edad': 'Edad',
            'alimentacion':'Alimentacion',
            'fecha_de_rescate':'Fecha de rescate',
            'raza': 'Raza',
            'enfermedades': 'Enfermedades',
            'imagen': 'Imagen',
            'vacunacion':'Vacunas aplicadas'
        }
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'edad': TextInput(attrs={'class':'form-control'}),
            'alimentacion':TextInput(attrs={'class':'form-control'}),
            'fecha_de_rescate':DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control','placeholder':'Fecha de rescate','type':'date'}),
            'raza': TextInput(attrs={'class':'form-control'}),
            'enfermedades': TextInput(attrs={'class':'form-control'}),
            'vacunacion': CheckboxSelectMultiple(choices=Vacunas)
        }

class CambiarComida(ModelForm):
    class Meta:
        model = RegistroMascota
        fields = ['alimentacion','id']
        labels = {
            'alimentacion':'',
            'id':'id'
        }
        widgets = {
                'ID': TextInput(
                attrs={
                    'readonly':'readonly',
                }
            )
        }