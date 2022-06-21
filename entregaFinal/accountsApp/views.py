from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import *
from .forms import *
from blogApp.models import *
# Create your views here.

def home(request):
    return render(request,"home.html")

def login_user(request):
    usuario = request.user    
    if request.method == 'POST':
        
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                perfil = Perfil.objects.filter(user=request.user.id)
                if(perfil.count() > 0):
                    perfil_nuevo = perfil[0]
                    if(perfil_nuevo.foto):
                        url = perfil_nuevo.foto.url
                    else:
                        url = ""
                    return render(request,'home.html',{"mensaje":f"Bienvenido {username}.","usuario":usuario,"url":url})
                else:
                    return render(request,'home.html',{"mensaje":f"Bienvenido {username}.","usuario":usuario})
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
            
            perfil = Perfil(user=form.save())
            perfil.save()
            
            return render(request, "home.html",{"mensaje":"Usuario creado"})
        
    else:
        form = UserCreationForm()
        
    return render(request,"registro.html",{"form":form})
@login_required
def logout(request):
    return render(request,'logout.html')

@login_required
def edit_user(request):
    usuario = request.user
    perfil = Perfil.objects.filter(user=request.user.id)
    if(perfil.count() > 0):
        perfil_nuevo = perfil[0]
        if(perfil_nuevo.foto):
            url = perfil_nuevo.foto.url
        else:
            url = ""
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST,request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.username = informacion["username"]
            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"]
            usuario.save()
                        
            perfil_actual = perfil[0] 
            perfil_actual.foto = informacion["foto"]            
            perfil_actual.save()
            
            url = perfil_actual.foto.url
            
            return render(request,"home.html",{"usuario":usuario,"url":url})
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email,'username':usuario.username,'last_name':usuario.last_name,'first_name':usuario.first_name})
    
    return render(request,'edit_user.html',{"miFormulario":miFormulario,"usuario":usuario,"url":url})