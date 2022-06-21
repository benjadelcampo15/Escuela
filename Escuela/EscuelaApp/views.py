from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request , 'EscuelaApp/inicio.html')

def profesores(request):
    return render(request , 'EscuelaApp/profesores.html')

def alumnos(request):
     return render(request , 'EscuelaApp/alumnos.html')

def cursos(request):
    return render(request , 'EscuelaApp/cursos.html')

def entregables(request):
     return render(request , 'EscuelaApp/entregables.html')