from django.shortcuts import render,redirect
from .forms import *


def listado_mascota(request):
    lista_mascota = RegistroMascota.objects.all()
    return render(request,'listado_mascota.html', {'lista_mascota': lista_mascota })


def registro_mascota(request):
    if request.method == 'POST':
        registro = Agregarmascota(request.POST, request.FILES)
        if registro.is_valid(): 
            registro.save()
            return redirect('home')
    else:
        registro = Agregarmascota()
    return render(request, 'registro_mascota.html', {'registro':registro})
