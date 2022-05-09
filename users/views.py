from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from mascota.models import *
from mascota.forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required  
def profile(request):
    lista_catalogo = RegistroMascota.objects.all()
    Nperfil = Profile.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Su cuenta ha sido actualizada')
            return redirect('profile')
    else:
        tipocomida = CambiarComida()
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form,
        'Nperfil':Nperfil,
        'lista_catalogo': lista_catalogo, 
    }


    return render(request, 'profile.html', context)

@login_required
def mismascotas (request):
    lista_catalogo = RegistroMascota.objects.all()
    if request.method == 'POST':
        tipocomida = CambiarComida(request.POST,instance=request.RegistroMascota)
        if tipocomida.is_valid():
            tipocomida.save()
            messages.success(request, f'La comida ha sido actualizada')
            return redirect('mismascotas')
    else:
        tipocomida= CambiarComida()
    context = {
        'tipocomida':tipocomida,
        'lista_catalogo': lista_catalogo, 
    }

    return render(request, 'mismascotas.html', context)   