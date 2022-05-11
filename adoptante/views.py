from django.shortcuts import render, redirect
from .models import *
from .forms  import *
from mascota.forms import *
from sre_constants import SUCCESS
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def solicitud(request):

    if request.method == 'POST':
        registro = SolicitudAdopcion(request.POST, request)
        if registro.is_valid():
            registro.save()
            return redirect('listado_mascota')
    else:
        registro = SolicitudAdopcion()
    return render(request, 'formulario.html', {'registro':registro})



class ListaAdoptantes(ListView):
    model = SolicitudAdop
    template_name = 'listado_adoptantes.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de adoptantes'
        return context

class EditarAdoptantes(UpdateView):
    model = SolicitudAdop
    form_class = VerAdoptante
    template_name = 'Editar_adoptantes.html'
    success_url = reverse_lazy('listado_adoptantes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Adoptante'
        context['entity']='SolicitudAdop'
        return context

