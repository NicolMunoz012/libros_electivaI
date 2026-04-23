from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/autor_list.html'
    context_object_name = 'autores'
class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'gestion/autor_create.html', {'form': form})
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autor_update.html', {'form': form})

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')

def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'gestion/libro_create.html', {'form': form})
def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/libro_update.html', {'form': form})

