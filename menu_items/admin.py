from django.contrib import admin

# Register your models here.
from .models import Category, MenuItem

admin.site.register([Category, MenuItem])
