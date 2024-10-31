from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        # img
        "price", #maybe update in future
    ]

admin.site.register(Product)