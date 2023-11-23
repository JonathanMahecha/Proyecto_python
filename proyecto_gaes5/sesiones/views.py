from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from proyecto_gaes5.views import *
from .forms import RegistrationForm  

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('Menu')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('Menu')
        else:
            messages.error(request, 'Ha ocurrido un error en el registro. Por favor, verifica los datos.')
    else:
        form = RegistrationForm()
    return render(request, 'registro.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')
