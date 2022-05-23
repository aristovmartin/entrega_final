from django.shortcuts import render
from .models import *
from .forms import *
from datetime import *

# Create your views here.

def about_me(request):
    return render(request,'about_me.html')

def pagina_blog(request,id):
    blog = Blog.objects.get(id_blog = id)
    today = datetime.now()
    return render(request,'page_blog.html',{"blog":blog})

def main(request):
    blogs = Blog.objects.all()
    today = datetime.now().date()
    return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today})

def crear_blog(request):
    if request.method == 'POST':
        formulario = BlogForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            blog = Blog(titulo=informacion['titulo'],subtitulo=informacion['subtitulo'],cuerpo=informacion['cuerpo'],autor=informacion['autor'],fecha=informacion['fecha'])
            blog.save()
            
            blogs = Blog.objects.all()
            today = datetime.now().date()
            return render(request,'main.html',{"blogs":blogs,"fecha_hoy":today}) 
    else:
        formulario = BlogForm()
        return render(request,'create_blog.html',{'formulario':formulario})  

#falta poder ver como editar foto
def editar_blog(request,id):
    blog = Blog.objects.get(id_blog = id)
    if request.method == 'POST':
         formulario = BlogForm(request.POST)
         if formulario.is_valid():
             informacion = formulario.cleaned_data
             
             blog.titulo = informacion["titulo"]
             blog.subtitulo = informacion["subtitulo"]
             blog.cuerpo = informacion["cuerpo"]
             blog.autor = informacion["autor"]
             blog.fecha = informacion["fecha"]
             
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
