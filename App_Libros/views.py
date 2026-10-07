from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm


def lista_libros(request):

    libros = Libro.objects.all()

    if request.method == 'POST':

        formulario = LibroForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_libros')

    else:

        formulario = LibroForm()

    return render(request, 'App_Libros/lista.html', {
        'libros': libros,
        'formulario': formulario
    })