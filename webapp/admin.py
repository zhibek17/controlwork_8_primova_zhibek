from django.contrib import admin
from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'image']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'category']
    fields = ['name', 'category', 'description', 'image']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'text', 'rating', 'moderated', 'created_at', 'updated_at']
    list_display_links = ['id', 'author', 'product']
    list_filter = ['moderated']
    search_fields = ['author__username', 'product__name', 'text']
    fields = ['author', 'product', 'text', 'rating', 'moderated', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
