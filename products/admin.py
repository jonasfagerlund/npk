from django.contrib import admin

from .models import Product, Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'npk',
    )

    

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
