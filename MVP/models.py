from django.db import models
from django.contrib.auth.models import User

class CuidadorMascotas(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    biografia = models.TextField()
    entrenamiento_cuidado_perros = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class DuenoMascota(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    dueno = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('canino', 'Canino'), ('felino', 'Felino')])
    raza = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

