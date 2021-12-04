from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sale', 'out_of_stock')
    list_editable = ('sale', 'out_of_stock')


admin.site.register(Product, ProductAdmin)
