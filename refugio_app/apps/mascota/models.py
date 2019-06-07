from django.db import models


class Mascota(models.Model):
    folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    fecha_rescate = models.DateField()
    
