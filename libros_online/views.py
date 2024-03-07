from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from gestion_libros.models import Libro
from gestion_libros.forms import FormularioContacto
from gestion_libros.forms import RegistroForm

def inicio(request):
    form_contacto = FormularioContacto()
    return render(request, 'inicio.html', {'form_contacto': form_contacto})

def buscar_libros(request):
    resultados = None
    if request.method == 'GET' and 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda')
        resultados = Libro.objects.filter(titulo__icontains=busqueda)
    return render(request, 'buscar_libros.html', {'resultados': resultados})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito_contacto')  
    else:
        form = FormularioContacto()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')
