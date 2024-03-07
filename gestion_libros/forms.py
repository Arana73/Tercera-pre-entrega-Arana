from django import forms
from django.contrib.auth.models import User
from gestion_libros.models import Libro
from .models import MensajeContacto

class RegistroForm(forms.ModelForm):
    username = forms.CharField(help_text='', label='Nombre de usuario')  # Sobrescribe el help_text para el campo username
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'email': 'Correo electrónico',
        }

class BusquedaLibrosForm(forms.Form):
    titulo = forms.CharField(required=False)
    autor = forms.CharField(required=False)
    genero = forms.CharField(required=False)


class FormularioContacto(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'mensaje']