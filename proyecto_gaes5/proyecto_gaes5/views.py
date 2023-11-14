from django.shortcuts import render 
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages



def inicio(request):
    return render(request, 'inicio.html', {
        #context
    })
    
def agendar(request):
    return render(request, 'agendar.html', {
        #context
    })
    
def asignarR(request):
    return render(request, 'asignarR.html', {
        #context
    })
    
def contactos(request):
    return render(request, 'contactos.html', {
        #context
    })
    
def crearCita(request):
    return render(request, 'crearCita.html', {
        #context
    })
    
def editarCita(request):
    return render(request, 'editarCita.html', {
        #context
    })
    
def form(request):
    return render(request, 'form.html', {
        #context
    })

def index(request):
    return render(request, 'index.html', {
        #context
    })
    
def indexr(request):
    return render(request, 'indexr.html', {
        #context
    })
    
def Menu(request):
    return render(request, 'Menu.html', {
        #context
    })
    
def menuAdmin(request):
    return render(request, 'MenuAdmin.html', {
        #context
    })
    
def verAgenda(request):
    return render(request, 'verAgenda.html', {
        #context
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('Menu')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })