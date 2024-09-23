

from django.http import HttpResponse
from django.shortcuts import render
from aboutus.models import About
from blogs.models import Category
from blogs.models import Blog

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
