from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import *
from mascota.models import *

class UserRegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(
                attrs={
                    'readonly':'readonly',
                }
            )
        }


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image':'image',
        }
   

class PwdResetForm(PasswordResetForm):
    email = EmailField(max_length=254, widget=TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

def clean_email(self):
    email = self.cleaned_data['email']
    u = User.objects.filter(email=email)
    if not u:
        raise forms.ValidationError(
            'Desafortunadamente no pudimos encontrar ningun usuario con este email')
    return email

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = CharField(
        label='Nueva Contraseña', widget=PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nueva Contraseña', 'id': 'form-newpass'}))
    new_password2 = CharField(
        label='Repite tu Contraseña', widget=PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nueva Contraseña', 'id': 'form-new-pass2'})) 


Vacunas={
        ('Parvovirus y moquillo','Parvovirus y moquillo'),
        ('Polivalente','Polivalente'),
        ('Contra la rabia','Contra la rabia'),
    }

class EditarMisMascota(ModelForm):
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
            'Nombreadoptante',
            'Apellidoadoptante',
            ]
        labels = {
            'nombre':'Nombre',
            'edad': 'Edad',
            'alimentacion':'Alimentacion',
            'fecha_de_rescate':'Fecha de rescate',
            'raza': 'Raza',
            'enfermedades': 'Enfermedades',
            'imagen': 'Imagen',
            'vacunacion':'Vacunas aplicadas',
            'Nombreadoptante':'Nombres del adoptante',
            'Apellidoadoptante':'Apellidos del adoptante',
        }
        widgets = {
            'nombre': TextInput(attrs={'readonly':'readonly'}),
            'edad': TextInput(attrs={'readonly':'readonly'}),
            'alimentacion':TextInput(attrs={'class':'form-control'}),
            'fecha_de_rescate':DateInput(format=('%Y-%m-%d'),attrs={'readonly':'readonly'}),
            'raza': TextInput(attrs={'readonly':'readonly'}),
            'enfermedades': TextInput(attrs={'readonly':'readonly'}),
            'vacunacion': CheckboxSelectMultiple(choices=Vacunas),
            'Nombreadoptante': TextInput(attrs={'readonly':'readonly'}),
            'Apellidoadoptante': TextInput(attrs={'readonly':'readonly'}),
        }