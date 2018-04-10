from django.contrib import admin

from .models import Todo   #import model from current app

# Register your models here.

admin.site.register(Todo) #registered model created in admin