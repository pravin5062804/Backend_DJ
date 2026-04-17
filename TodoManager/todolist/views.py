from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        'page':'home',
    }
    return render(request,"todolist.html",context)

def contact(request):
     context={
        'page':'contact',
        }
     return render(request,"contact.html",context)

def about(request):
     context={
        'page':'about',
    }
     return render(request,"about.html",context)

def blog(request):
     context={
        'page':'blog',
    }
     return render(request,"blog.html",context)

