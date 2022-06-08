from django.urls import path
from LiderApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('cursos/', views.cursos, name='cursos'),
    path('contacto/', views.contacto, name='contacto'),
    path('busquedaCurso/', views.busquedaCurso, name='busquedaCurso'),
    path('resultadoCurso/', views.resultadoCurso, name='resultadoCurso'),
    path('busquedaNewsletter/', views.busquedaNewsletter, name= 'busquedaNewsletter'),
    path('resultadoNewsletter/', views.resultadoNewsletter, name= 'resultadoNewsletter'),
]