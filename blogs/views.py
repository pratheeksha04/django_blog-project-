from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category

# Create your views here.

def posts_by_category(request,category_id):
    #fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published',Category=category_id)#category is from models.py
    # category=Category.objects.get(pk=category_id)#get for grtting single obj
    #if catogory id is not presnt then error
    # categories=Category.objects.all() for multiple pages wecant do that so use context processor
    # try:
    #     category=Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    category=get_object_or_404(Category, pk=category_id)#design custom 404 error page
    context={
        "posts":posts,
        "category":category,
       
    }
    return render(request,'posts_by_category.html',context)#FOR posts_by_category.html PAGE WILL PASS CONTEXT
