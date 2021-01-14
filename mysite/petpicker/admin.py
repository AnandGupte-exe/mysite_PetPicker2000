from django.contrib import admin
from .models import petpicker_Model
from .models import MyModel

# Register your models here.

admin.site.register(petpicker_Model)

admin.site.register(MyModel)
