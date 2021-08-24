from django.contrib import admin
from .models import Product, Rating 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    search_fields = ['name', 'description']


admin.site.register(Rating)