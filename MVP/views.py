from django.shortcuts import render, redirect
from .forms import CuidadorForm, DuenoForm, MascotaForm
from .utils import buscar_cuidador_por_nombre

def home(request):
    contexto = {
        'titulo': 'Pet Sitter para tus mascotas',  # Puedes pasar este título al contexto
    }
    return render(request, 'home.html', contexto)

def agregar_cuidador(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')  # Redirige a la vista deseada después de guardar
    else:
        form = CuidadorForm()
    return render(request, 'agregar_cuidador.html', {'form': form})

def agregar_dueno(request):
    if request.method == 'POST':
        form = DuenoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')  # Redirige a la vista deseada después de guardar
    else:
        form = DuenoForm()
    return render(request, 'agregar_dueno.html', {'form': form})

def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')  # Redirige a la vista deseada después de guardar
    else:
        form = MascotaForm()
    return render(request, 'agregar_mascota.html', {'form': form})

def buscar_cuidador(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cuidadores = buscar_cuidador_por_nombre(nombre)
        
        return render(request, 'buscar_cuidador.html', {'cuidadores': cuidadores})
    
    return render(request, 'home.html')