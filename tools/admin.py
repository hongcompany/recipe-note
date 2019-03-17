from django.contrib import admin

# Register your models here.
from .models import Tools


class ToolsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


admin.site.register(Tools, ToolsAdmin)
