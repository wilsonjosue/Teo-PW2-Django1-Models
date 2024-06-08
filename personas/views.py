from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm, PersonaForm
from .models import Persona
# Create your views here.

def registro(request): # Se implementa el registro para el usuario nuevo en un html
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register.html', {'form': form})

def login_view(request): # Se implementa la funcion login
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request): # Se implementa el index donde se presentara la pantalla principal
    personas = Persona.objects.all()
    return render(request, 'index.html', {'personas': personas})

def agregar_persona(request):# Se implementa la funcion de agregar a una persona
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()
    return render(request, 'agregar_persona.html', {'form': form})
