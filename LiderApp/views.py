import email
from django.http import HttpResponse
from django.shortcuts import render
from LiderApp.forms import *
from LiderApp.models import *

# Create your views here.

def prueba(request):
    return render(request, 'LiderApp/padre.html')

def inicio(request):
    return render(request, 'LiderApp/inicio.html')

def newsletter(request):
    if request.method == "POST":
        miFormulario= NewsletterFormulario(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            nombre= request.POST['nombre']
            apellido= request.POST['apellido']
            email= request.POST['email']
            profesion= request.POST['profesion']
            pais= request.POST['pais']
            newsletter= Newsletter(nombre=nombre, apellido=apellido, email=email, profesion=profesion, pais=pais)
            newsletter.save()
            return render(request, "LiderApp/inicio.html")
    else:
        miFormulario = NewsletterFormulario()
    return render(request, 'LiderApp/newsletter.html', {'miFormulario':miFormulario})

def busquedaNewsletter(request):
    return render(request, 'LiderApp/busquedaNewsletter.html')

def resultadoNewsletter(request):
    if request.GET['pais']:
        pais = request.GET['pais']
        paises = Newsletter.objects.filter(pais__icontains=pais)
        return render(request, "LiderApp/resultadoNewsletter.html", {"paises":paises, "pais":pais})
    else:
        respuesta = "No enviaste datos"
    return render(request, "LiderApp/resultadoNewsletter.html", {"respuesta":respuesta})   
    
def cursos(request):
    if request.method == "POST":
        cursoFormulario= CursosFormulario(request.POST)

        if cursoFormulario.is_valid():
            informacion= cursoFormulario.cleaned_data
            nombre= request.POST['nombre']
            apellido= request.POST['apellido']
            email= request.POST['email']
            curso_de_interes= request.POST['curso']
            curso= Cursos(nombre=nombre, apellido=apellido, email=email, curso_de_interes=curso_de_interes)
            curso.save()
            return render(request, "LiderApp/inicio.html")
    else:
        cursoFormulario = CursosFormulario()
    return render(request, 'LiderApp/cursos.html', {'cursoFormulario':cursoFormulario})

def contacto(request):
    if request.method == "POST":
        contactoFormulario= ContactoFormulario(request.POST)

        if contactoFormulario.is_valid():
            informacion= contactoFormulario.cleaned_data
            nombre= request.POST['nombre']
            apellido= request.POST['apellido']
            email= request.POST['email']
            telefono= request.POST['telefono']
            solicitud= request.POST['solicitud']
            contacto= Contacto(nombre=nombre, apellido=apellido, email=email, telefono=telefono, solicitud=solicitud)
            contacto.save()
            return render(request, "LiderApp/inicio.html")
    else:
        contactoFormulario = ContactoFormulario()
    return render(request, 'LiderApp/contacto.html',{'contactoFormulario':contactoFormulario})

def busquedaCurso(request):
    return render(request, "LiderApp/busquedaCurso.html")

def resultadoCurso(request):

    if request.GET['curso']:
        curso = request.GET['curso']
        cursos = Cursos.objects.filter(curso_de_interes__icontains=curso)
        return render(request, "LiderApp/resultadosBusqueda.html", {"cursos":cursos, "curso":curso})
    else:
        respuesta = "No enviaste datos"
    return render(request, "LiderApp/resultadosBusqueda.html", {"respuesta":respuesta})