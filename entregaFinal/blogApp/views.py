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

#muestro los blogs en el main
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
            return render(request,'main.html')
    else:
        formulario = BlogForm()
        return render(request,'create_blog.html',{'formulario':formulario})   