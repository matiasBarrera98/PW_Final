from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.db.models import CharField, IntegerField

# Create your models here.

class Animal (models.Model):
    idAnimal = models.IntegerField(primary_key=True, verbose_name='Id de Animal')
    nombreAnimal = models.CharField(max_length=50, verbose_name='Nombre de Animal')

    def __str__(self):
        return self.nombreAnimal

class Mascota (models.Model):
    idMascota = models.IntegerField(primary_key=True, verbose_name='Id de Mascota')
    nombre = models.CharField(max_length=30, verbose_name='Nombre de Mascota')
    telefonoDuenio = models.CharField(max_length=15, verbose_name='Telefono del Dueño')
    idAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

