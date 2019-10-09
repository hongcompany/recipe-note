from django.contrib import admin

# Register your models here.
from .models import *


class ToolsInline(admin.TabularInline):
    model = RecipeTools
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', "recipe_tools", "category_info", "created_at", "is_template", "is_deleted"]
    list_editable = ["is_deleted"]
    inlines = [ToolsInline]


class IngredientsInline(admin.TabularInline):
    model = RecipeDetailsIngredients
    extra = 3


class RecipeDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'description', 'timer', 'type', 'recipe_details_ingredients']
    list_editable = ['description', 'timer', 'type']
    model = RecipeDetails

    inlines = [IngredientsInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeDetails, RecipeDetailsAdmin)
