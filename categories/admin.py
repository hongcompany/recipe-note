from django.contrib import admin

# Register your models here.
from .models import Category


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at', 'is_deleted']
    list_editable = ['name', 'is_deleted']


admin.site.register(Category, CategoriesAdmin)