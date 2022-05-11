from django.urls import path
from .views import *


urlpatterns = [
    path('', listado_mascota, name='listado_mascota'),
    path('registro_mascota/', CreateMascota.as_view(), name='registro_mascota'),
    path('listadoT_mascotas/', TodasMascotaslist.as_view(), name='listadotodasmascotas')
]