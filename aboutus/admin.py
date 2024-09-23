from django.contrib import admin
from django.http import HttpRequest

from .models import About
#to make about has only1 obj
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=About.objects.all().count()
        if count ==0:
            return True 
        return False
# Register your models here.
admin.site.register(About,AboutAdmin)
