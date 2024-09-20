

from .models import Category

#mention this in settings.py under templates
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)