from django.contrib import admin
<<<<<<< HEAD
from .models import Moto

# Register your models here.
class MotoAdmin(admin.ModelAdmin):
    list_display = (
        'reference',
        'trademark',
        'model',
        'price',
        'image',
        'supplier',
    )
    
# Register your models here.
admin.site.register(Moto, MotoAdmin)
=======

# Register your models here.
>>>>>>> a3319ba (initialize Django project structure with basic settings and configurations)
