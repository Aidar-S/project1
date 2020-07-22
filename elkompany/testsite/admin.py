from django.contrib import admin
from .models import Tovar, Category

# Register your models here.


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'price']
    list_filter = ['price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
