from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from .models import *

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