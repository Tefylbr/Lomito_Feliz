from django.shortcuts import render, redirect
from .models import *
from .forms  import *
from mascota.forms import *

def solicitud(request):

    if request.method == 'POST':
        registro = SolicitudAdopcion(request.POST, request)
        if registro.is_valid():
            registro.save()
            return redirect('listado_mascota')
    else:
        registro = SolicitudAdopcion()
    return render(request, 'formulario.html', {'registro':registro})
