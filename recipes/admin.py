from django.contrib import admin

# Register your models here.
from .models import *


class SummaryInline(admin.TabularInline):
    model = RecipeSummary


class ToolsInline(admin.TabularInline):
    model = RecipeTools
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', "recipe_summary", "recipe_tools", "category_info", "created_at", "is_template", "is_deleted"]
    list_editable = ['is_template', "is_deleted"]
    inlines = [SummaryInline, ToolsInline]


admin.site.register(Recipe, RecipeAdmin)
