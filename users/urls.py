from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('mismascotas/', views.mismascotas, name='mismascotas')
]