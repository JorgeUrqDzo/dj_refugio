from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


class Solicitud(models.Model):
	persona = models.ForeignKey(
	    Persona, null=True, blank=True, on_delete=models.PROTECT)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()
