from django.contrib import admin
from reviews.models import ProductReview
# Register your models here.
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'comment']
    search_fields = ['user', 'rating']
    list_filter = ['user', 'rating']

admin.site.register(ProductReview, ProductReviewAdmin)