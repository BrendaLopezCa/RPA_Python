from multiprocessing import context
from django.shortcuts import render

from lenguajes_modernos.aplicaciones.principal.forms import AlumnoForm
from .models import Alumno

def inicio(request):
    alumnos = Alumno.objects.all()
    contexto = {
        'alumnos':alumnos
    }
    return render(request, 'index.html')

def crearAlumno(request):
    form = AlumnoForm()
    contexto = {
        'form':form
    }
    return render(request,'crear_alumno.html', contexto)
