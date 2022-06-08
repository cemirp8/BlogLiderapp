from django.db import models
# Create your models here.

class Newsletter(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    pais=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.profesion)

class Cursos(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    curso_de_interes=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.curso_de_interes)

class Contacto(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    telefono=models.CharField(max_length=15)
    solicitud=models.CharField(max_length=140)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.solicitud)