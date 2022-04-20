from django.contrib import admin
from . models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price',)
    # list_filter = ('', '','')
    # search_fields = ('title','content')