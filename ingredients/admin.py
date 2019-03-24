from django.contrib import admin

# Register your models here.
from .models import Ingredients


class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


admin.site.register(Ingredients, IngredientsAdmin)
