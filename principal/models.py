from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models

class Alumno(models.Model):
    matricula = models.AutoField(primary_key= True)
    nombres = models.CharField(max_lenght = 120)
    apellidos = models.CharField(max_length = 120)
    facultad = models.CharField(max_length = 100)
    carrera = models.CharField(max_length =90)
    correo = models.EmailField(max_length = 200)

    def __str__(self):
        return self.nombres
