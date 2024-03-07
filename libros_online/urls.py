from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar_libros, name='buscar'),
    path('registro/', views.registro, name='registro'),
    path('libros/', views.lista_libros, name='libros'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/exito/', views.exito, name='exito_contacto'),
    path('registro/', views.registro, name='registro'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]
