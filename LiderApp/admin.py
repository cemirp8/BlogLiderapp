from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Newsletter)
admin.site.register(Cursos)
admin.site.register(Contacto)