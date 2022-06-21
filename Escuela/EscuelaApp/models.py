from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models

# Create your models here.

class Estudiante(models.Model) :
    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=30)

    email = models.EmailField()

class Profesor(models.Model) :
    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=30)

    profesion = models.CharField(max_length=30)

    email = models.EmailField()

class Curso(models.Model):
    nombre = models.CharField(max_length=30)

    comision = models.IntegerField()

class entregable(models.Model):
    nombre = models.CharField(max_length=30)

    fecha_entrega = models.DateField()

    entregado = models.BooleanField()

