from django.contrib import admin
from .models import Category
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}#as we write title slug should be generated automatically
    list_display=('title','Category','author','status','is_featured',)
    search_fields=('id','title','Category__category_name','status',)#category foreign key
    list_editable=('is_featured',)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)