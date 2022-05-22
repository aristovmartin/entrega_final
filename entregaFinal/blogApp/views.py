from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def about_me(request):
    return render(request,'about_me.html')

def pagina_blog(request):
    return render(request,'page.html')

#muestro los blogs en el main
def main(request):
    blogs = Blog.objects.all()
    return render(request,'main.html',{"blogs":blogs})