from django import forms
from django.shortcuts import redirect, render
from .models import Alumno
from .forms import AlumnoForm, AlumnoForm

def inicio(request):
    alumnos=Alumno.objects.all()
    contexto={
        'alumnos':alumnos
    }
    return render(request, 'index.html', contexto)

def crearAlumno(request):
    if request.method=='GET':
        form=AlumnoForm()
        contexto={
            'form':form
        }
    else:
        form=AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_alumno.html', {'form':form})

def editarAlumno(request, matricula):
    alumno=Alumno.objects.get(matricula=matricula)
    if request.method=='GET':
        form=AlumnoForm(instance=alumno)
        contexto={
            'form':form
        }
    else:
        form=AlumnoForm(request.POST, instance=alumno)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_alumno.html', contexto)

def eliminarAlumno(request, matricula):
    alumno=Alumno.objects.get(matricula=matricula)
    alumno.delete()
    return redirect('index')