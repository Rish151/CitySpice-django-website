from django.contrib import admin
from .models import Product, Contact_Query

# Register your models here.
admin.site.register(Product) #for product register through admin and makemigrations through console
admin.site.register(Contact_Query)
