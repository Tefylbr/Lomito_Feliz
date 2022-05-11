from django.urls import path
from mascota.views import *
from .views import *


urlpatterns = [
    path('', profile, name='profile'),
    path('mismascotas/', Mismascotaslist.as_view(), name='mismascotas')
]