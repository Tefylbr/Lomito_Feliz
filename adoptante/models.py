from django.db import models


class SolicitudAdop (models.Model):
    Nombre     = models.CharField(max_length=50)
    Edad       = models.CharField(max_length=50)
    Correo     = models.EmailField()
    Telefono   = models.CharField(max_length=8)
    Domicilio  = models.CharField(max_length=100)
    NumeroMasc = models.IntegerField()
    Razones    = models.CharField(max_length=150)
    Estado   = models.CharField(max_length=15, default='En proceso')


    def __str__(self):
        return self.Nombre

    def save(self, *args, **kwargs):
        super(SolicitudAdop, self).save(*args, **kwargs)