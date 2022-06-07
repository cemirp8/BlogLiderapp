from django import forms

class NewsletterFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=30)

class CursosFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    curso=forms.CharField(max_length=40)

class ContactoFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    telefono=forms.CharField(max_length=15)
    solicitud=forms.CharField(max_length=140)