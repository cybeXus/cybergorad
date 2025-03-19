from django.shortcuts import render
from .models import Formation
from .models import Blog

def home(request):
    formations = Formation.objects.all() 
    blogs = Blog.objects.all()
    return render(request, 'home/index.html', {'formations': formations, 'blogs': blogs})
