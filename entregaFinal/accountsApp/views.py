from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,"home.html")

def login_user(request):
    if request.method == 'POST':
        
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request,'home.html',{"mensaje":f"Bienvenido {username}."})
            else:
                return render(request,"home.html",{"mensaje":"Error, datos incorrectos."})
        else:
            return render(request,"home.html",{"mensaje":"Error,formulario incorrecto."})
        
    form = AuthenticationForm()
    
    return render(request,"login.html",{"form":form})

def registro(request):
    
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            usernames = form.cleaned_data["username"]
            form.save()
            return render(request, "home.html",{"mensaje":"Usuario creado"})
        
    else:
        form = UserCreationForm()
        
    return render(request,"registro.html",{"form":form})

def logout(request):
    return render(request,'logout.html')

def edit_user(request):
    usuario = request.user
    
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.username = informacion["username"]
            last_name = informacion["last_name"]
            first_name = informacion["first_name"]
            usuario.save()
            
            return render(request,"home.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email,'nombre_usuario':usuario.nombre_usuario})
    
    return render(request,'edit_user.html',{"miFormulario":miFormulario,"usuario":usuario})