from django.contrib import admin
from products.models import ChocolateProduct, Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['chocolate_product', 'name', 'description', 'price']
    search_fields = ['chocolate_product']
    list_filter = ['chocolate_product', 'name']

admin.site.register(Category, CategoryAdmin)


class ChocolateProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'existence', 'product_type']
    search_fields = ['name', 'product_type']
    list_filter = ['name', 'product_type']


admin.site.register(ChocolateProduct, ChocolateProductAdmin)