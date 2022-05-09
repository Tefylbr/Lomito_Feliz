from django.urls import path
from . import views


urlpatterns = [
    path('', views.listado_mascota, name='listado_mascota'),
    path('registro_mascota/', views.registro_mascota, name='registro_mascota'),
]