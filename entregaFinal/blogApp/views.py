from django.shortcuts import render
from .models import *
from .forms import *
from datetime import *
from django.contrib.auth.decorators import *
from django.contrib.auth.models import User


# Create your views here.

def about_me(request):
    return render(request,'about_me.html')

def pagina_blog(request,id):
    blog = Blog.objects.get(id_blog = id)
    today = datetime.now()
    return render(request,'page_blog.html',{"blog":blog})

def main(request):
    blogs = Blog.objects.all()
    perfiles = Perfil.objects.filter(user=request.user.id)
    today = datetime.now().date()    
    if(perfiles.count() > 0):
        perfil = perfiles[0]      
        if(perfil.foto):
            url = perfil.foto.url
        else:
            url = ""  
        return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today,"url":url,"username":perfil.user.username})
    else:
        return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today})
        
        
@login_required
def crear_blog(request):
    if request.method == 'POST':
        formulario = BlogForm(request.POST,request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            blog = Blog(titulo=informacion['titulo'],subtitulo=informacion['subtitulo'],cuerpo=informacion['cuerpo'],autor=request.user.username,fecha=datetime.now(),foto=informacion['foto'])
            blog.save()
            
            blogs = Blog.objects.all()
            today = datetime.now().date()
            return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today}) 
    else:
        formulario = BlogForm()
        return render(request,'create_blog.html',{'formulario':formulario})  

def editar_blog(request,id):
    blog = Blog.objects.get(id_blog = id)
    if request.method == 'POST':
         formulario = BlogForm(request.POST,request.FILES)
         if formulario.is_valid():
             informacion = formulario.cleaned_data
             
             blog.titulo = informacion["titulo"]
             blog.subtitulo = informacion["subtitulo"]
             blog.cuerpo = informacion["cuerpo"]
             blog.autor = informacion["autor"]
             blog.fecha = informacion["fecha"]
             blog.foto = informacion["foto"]
             blog.save()

             blogs = Blog.objects.all()
             today = datetime.now().date()
             return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today}) 
    else:
        formulario = BlogForm(initial={'titulo':blog.titulo,'subtitulo':blog.subtitulo,
                                       'cuerpo':blog.cuerpo,'autor':blog.autor,
                                       'fecha':blog.fecha})
        return render(request,'editar_blog.html', {"formulario":formulario, "id":id})
             
def eliminar_blog(request,id):
    blog = Blog.objects.get(id_blog = id)
    blog.delete()
    
    blogs  = Blog.objects.all()
    
    return render(request,'main.html',{"blogs":blogs})

@login_required
def mensajes(request):
    mensajes_enviados = Mensaje.objects.filter(usuario_origen = request.user.username)
    mensajes_recibidos = Mensaje.objects.filter(usuario_destino = request.user.username)
    return render(request,'mensajes.html',{"mensajes_enviados":mensajes_enviados,"mensajes_recibidos":mensajes_recibidos})

@login_required
def enviar_mensajes(request):
    if request.method == 'POST':
        formulario = MensajeForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario_origen = User.objects.filter(username=request.user.username)
            usuario_destino = User.objects.filter(username=informacion['usuario_destino'])
            if(usuario_origen.count() > 0 and usuario_destino.count() > 0):
                mensaje = Mensaje(usuario_origen=request.user.username,usuario_destino=informacion["usuario_destino"],texto=informacion["texto"])
                mensaje.save()
                
                blogs = Blog.objects.all()
                perfiles = Perfil.objects.filter(user=request.user.id)
                today = datetime.now().date()
                if(perfiles.count() > 0):
                    perfil = perfiles[0]
                    return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today,"url":perfil.foto.url,"username":perfil.user.username})
                else:
                    return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today})

            else:
                formulario = MensajeForm()
                return render(request,'enviar_mensaje.html',{'formulario':formulario,"mensaje":"No existe alguno de lo usuarios ingresados"})
        else:#No es valido el formulario
            formulario = MensajeForm(initial={'usuario_origen':request.user.username})
            return render(request,'enviar_mensaje.html',{'formulario':formulario})
    else:
        formulario = MensajeForm(initial={'usuario_origen':request.user.username})
        return render(request,'enviar_mensaje.html',{'formulario':formulario})
    
def borrar_foto(request,id):
    blog = Blog.objects.get(id_blog=id)
    if(blog):
        blog.foto = " "
        blog.save()

    blogs = Blog.objects.all()
    perfiles = Perfil.objects.filter(user=request.user.id)
    today = datetime.now().date()    
    if(perfiles.count() > 0):
        perfil = perfiles[0]      
        if(perfil.foto):
            url = perfil.foto.url
        else:
            url = ""  
        return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today,"url":url,"username":perfil.user.username})
    else:
        return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today})