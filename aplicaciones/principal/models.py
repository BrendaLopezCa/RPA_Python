from django.db import models

class Alumno(models.Model):
    matricula=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    facultad=models.CharField(max_length=50)
    carrera=models.CharField(max_length=50)
    correo=models.EmailField(max_length=150)

    def __str__(self):
        return self.nombres