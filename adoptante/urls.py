from django.urls import path
from .views import *

urlpatterns = [
    path('', ListaAdoptantes.as_view(), name='listado_adoptantes'),
    path('ver_adoptante/<int:pk>',EditarAdoptantes.as_view(), name='ver_adoptante')


]