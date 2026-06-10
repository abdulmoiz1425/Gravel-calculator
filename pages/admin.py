from django.contrib import admin
from .models import PageContent


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page', 'updated_at')
    readonly_fields = ('updated_at',)
