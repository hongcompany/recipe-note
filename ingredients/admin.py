from django.contrib import admin

# Register your models here.
from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


admin.site.register(Ingredient, IngredientAdmin)
