from django.contrib import admin
from .models import ContactMessage, PageContent


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'subject')
    list_editable = ('is_read',)
    search_fields = ('full_name', 'email', 'message')
    readonly_fields = ('full_name', 'email', 'subject', 'message', 'created_at')
