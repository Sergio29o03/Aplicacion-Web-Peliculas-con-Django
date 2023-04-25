import re
from django.shortcuts import redirect, render,redirect
from .models import Curso
from django.contrib import messages 


def vistapeliculas():
    return render("vistapeliculas.html")


def home(request):
    PeliculasListadas=Curso.objects.all()
    return render(request, "gestionPeliculas.html",{"Peliculas": PeliculasListadas})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    genero=request.POST['txtGenero']
    año=request.POST['numAño']


    curso=Curso.objects.create(codigo=codigo,nombre=nombre,genero=genero,año=año)
    return redirect('/')

def edicionCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})


def comentarioCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, "ComentariosPeliculas.html" , {"curso":curso})




def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    genero=request.POST['txtGenero']
    año=request.POST['numAño']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.genero = genero
    curso.año = año 

    curso.save()
    return redirect('/')




def eliminacionCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

