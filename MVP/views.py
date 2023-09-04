from django.shortcuts import render, redirect, get_object_or_404
from .forms import CuidadorForm, DuenoForm, MascotaForm, UserRegistrationForm, UserEditForm
from .utils import buscar_cuidador_por_nombre
from .models import CuidadorMascotas, DuenoMascota, Mascota
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def home(request):
    contexto = {
        'titulo': 'Pet Sitter para tus mascotas',  # Puedes pasar este título al contexto
    }
    return render(request, 'home.html', contexto)

#--CRUD para cuidadores-- 

@login_required
def agregar_cuidador(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('petsitters') # redirige a la misma vista
    else:
        form = CuidadorForm()
    return render(request, 'agregar_cuidador.html', {'form': form})

@login_required
def petsitters(request):
    cuidadores = CuidadorMascotas.objects.all()
    return render(request, 'petsitters.html', {'cuidadores': cuidadores})

@login_required
def editar_cuidador(request, cuidador_id):
    cuidador = get_object_or_404(CuidadorMascotas, id=cuidador_id)

    if request.method == 'POST':
        form = CuidadorForm(request.POST, instance=cuidador)
        if form.is_valid():
            form.save()
            return redirect('petsitters')  # Redirige a la vista de la lista de cuidadores
    else:
        form = CuidadorForm(instance=cuidador)
    
    contexto = {
        'form': form,
        'accion': 'Editar Cuidador'  # Etiqueta para el botón del formulario
    }

    return render(request, 'editar_cuidador.html', contexto)

@login_required
def eliminar_cuidador(request, cuidador_id):
    # Obtén el cuidador por su ID o muestra un error 404 si no existe
    cuidador = get_object_or_404(CuidadorMascotas, pk=cuidador_id)

    if request.method == 'POST':
        # Si se confirma la eliminación, elimina el cuidador y redirige a la lista de cuidadores
        cuidador.delete()
        return redirect('petsitters')
    return redirect('petsitters')


#funcion de buscar cuidador de mascota

def buscar_cuidador(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cuidadores = buscar_cuidador_por_nombre(nombre)
        return render(request, 'buscar_cuidador.html', {'cuidadores': cuidadores})
    
    return render(request, 'home.html')

#--CRUD para dueños de mascotas-- 

class DuenoMascotaList(LoginRequiredMixin, ListView):
    model = DuenoMascota
    template_name = "petowners.html"

class DuenoMascotaCreate(LoginRequiredMixin, CreateView):
    model = DuenoMascota
    fields = ['nombre','correo_electronico','telefono','direccion']
    success_url = reverse_lazy('petowners')
    template_name = "agregar_dueno.html"

class DuenoMascotaUpdate(LoginRequiredMixin, UpdateView):
    model = DuenoMascota
    fields = ['nombre','correo_electronico','telefono','direccion']
    success_url = reverse_lazy('petowners')
    template_name = "update_dueno.html"

class DuenoMascotaDelete(LoginRequiredMixin, DeleteView):
    model = DuenoMascota
    success_url = reverse_lazy('petowners')

#--CRUD para mascotas-- 

class MascotaList(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = "mascotas.html"

class MascotaCreate(LoginRequiredMixin, CreateView):
    model = Mascota
    fields = ['nombre','dueno','tipo','raza', 'edad']
    success_url = reverse_lazy('mascotas')
    template_name = "agregar_mascota.html"

class MascotaUpdate(LoginRequiredMixin, UpdateView):
    model = Mascota
    fields = ['nombre','dueno','tipo','raza', 'edad']
    success_url = reverse_lazy('mascotas')
    template_name = "update_mascota.html"

class MascotaDelete(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('mascotas')


#login-register-edición

#login

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Iniciar sesión y redirigir al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia 'inicio' a la URL a la que deseas redirigir después del inicio de sesión exitoso
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

#registro

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige al inicio de sesión después del registro
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

#edición del usuario

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return redirect('editarperfil')
        else:
            return render(request,"editarperfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "editarperfil.html", {'form': form, 'usuario': usuario.username})

