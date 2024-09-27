

from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from aboutus.models import About
from blogs.models import Category
from blogs.models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

#whatever changes u need to make in home page update here example aboutus app models.py
def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True)
    posts=Blog.objects.filter(is_featured=False,status='Published')

    try:
        about=About.objects.get()#only 1 obj is there in admin#try works only with .get() not with .all()
    except:
        about=None
    # print(categories)
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about
    }
    return render(request,'home.html',context)

def register(request):
    if request.method=="POST":
        #post req to send  register fields with data)
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        #get req to load empty register fields
        form=RegistrationForm()
    context={
        'form':form,
        }    
    return render(request,'register.html',context )

def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')

    form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')