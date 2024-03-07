from django.contrib import admin
from .models import Libro
from .models import MensajeContacto
from django.contrib.auth.models import User

admin.site.register(Libro)
admin.site.register(MensajeContacto)

