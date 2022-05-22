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