from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"