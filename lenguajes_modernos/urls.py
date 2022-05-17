from django.contrib import admin
from django.db import models
from django.urls import path
from aplicaciones.principal.views import inicio, crearAlumno, editarAlumno, eliminarAlumno
#from aplicaciones.principal.class_view import AlumnoList, AlumnoCreate, AlumnoUpdate, AlumnoDelete   Vistas en clases

"""
Vistas en clases

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AlumnoList, name='index'),
    path('crear_alumno/', AlumnoCreate, name='crear_alumno'),
    path('editar_alumno/<int:matricula>/', AlumnoUpdate, name='editar_alumno'),
    path('eliminar_alumno/<int:matricula>/', AlumnoDelete, name='eliminar_alumno')
]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('crear_alumno/', crearAlumno, name='crear_alumno'),
    path('editar_alumno/<int:matricula>/', editarAlumno, name='editar_alumno'),
    path('eliminar_alumno/<int:matricula>/', eliminarAlumno, name='eliminar_alumno')
]