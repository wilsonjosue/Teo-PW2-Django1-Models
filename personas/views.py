from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegistroUsuarioForm, PersonaForm
from .models import Persona
# Create your views here.

def registro(request): # Se implementa el registro para el usuario nuevo en un html
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'El nombre de usuario ya está tomado')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'El correo electrónico ya está registrado')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'Usuario creado exitosamente')
                return redirect('login')
        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login_view(request): # Se implementa la funcion login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credenciales inválidas')
            return redirect('login')
    else:
        return render(request, 'login.html')  

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

def logout_view(request):
    auth.logout(request)
    return redirect('/')
