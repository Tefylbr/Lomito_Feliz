from django.db import models
from django.utils import timezone
from PIL import Image

class RegistroMascota (models.Model):
    imagen           = models.ImageField(default='default.jpg', upload_to='fotos_mascotas')
    alimentacion     = models.CharField(max_length= 50)
    vacunacion       = models.CharField(max_length= 100)
    edad             = models.CharField(max_length= 30)
    fecha_de_rescate = models.DateTimeField(default=timezone.now)
    raza             = models.CharField(max_length= 50)
    enfermedades     = models.CharField(max_length= 50)
    nombre           = models.CharField(max_length= 50)
    Nombreadoptante        = models.CharField(default='Disponible', max_length= 50)
    Apellidoadoptante        = models.CharField(default='Disponible', max_length= 50)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        super(RegistroMascota, self).save(*args, **kwargs)

        img = Image.open(self.imagen.path)
        if (img.height > 300  or img.width >300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagen.path)

