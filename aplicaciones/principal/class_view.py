from django.db import models
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AlumnoForm
from .models import Alumno

class AlumnoList(ListView):
    model=Alumno
    template_name='index.html'

class AlumnoCreate(CreateView):
    model=Alumno
    form_class=AlumnoForm
    template_name='crear_alumno.html'
    succes_url=reverse_lazy('index')

class AlumnoUpdate(UpdateView):
    model=Alumno
    form_class=AlumnoForm
    template_name='crear_alumno.html'
    succes_url=reverse_lazy('index')

class AlumnoDelete(DeleteView):
    model=Alumno
    template_name='verificacion.html'
    succes_url=reverse_lazy('index')