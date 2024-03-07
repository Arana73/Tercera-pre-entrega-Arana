from django.db import models
from django import forms

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.nombre} ({self.email})'

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'gestion_libros'

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'mensaje']
