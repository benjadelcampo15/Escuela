
from django import views
from django.contrib import admin
from django.urls import path
from EscuelaApp import views

urlpatterns = [
    path('', views.inicio),

    path('profesores/', views.profesores),

    path('alumnos/' , views.alumnos),

    path('cursos/', views.cursos ),

    path('entregables/' , views.entregables),

]
