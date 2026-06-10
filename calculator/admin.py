from django.contrib import admin
from .models import GravelType


@admin.register(GravelType)
class GravelTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'density', 'typical_use', 'is_active', 'order')
    list_editable = ('density', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('order', 'name')
