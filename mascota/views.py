from sre_constants import SUCCESS
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from matplotlib.style import context
from .forms import *
from django.views.generic import UpdateView, ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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


class CreateMascota(CreateView):
    model = RegistroMascota
    form_class = Agregarmascota
    template_name = 'registro_mascota.html'
    success_url = reverse_lazy('listado_mascota')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Registrar una mascota'
        return context


class TodasMascotaslist(ListView):
    model = RegistroMascota
    template_name = 'TodasMascotas.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de mascotas'
        return context
