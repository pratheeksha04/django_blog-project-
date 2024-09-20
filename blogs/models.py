from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#register this model in admin.py
class Category(models.Model):
    category_name=models.CharField(max_length=20,unique=True)
    creted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

#dropdown
STATUS_CHOICES=(
    ("Draft","Draft"),
    ("Published","Published"),
)


class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)#fk stores the id of pk #django will store it as category_id 
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
    is_featured=models.BooleanField(default=False)
    creted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



