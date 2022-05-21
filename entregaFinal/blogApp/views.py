from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main.html')

def about_me(request):
    return render(request,'about_me.html')

def pagina_blog(request):
    return render(request,'page.html')