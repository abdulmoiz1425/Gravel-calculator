from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    def ready(self):
        super().ready()
        from django.contrib import admin
        admin.site.site_header = 'Gravel Calculator Pro Admin'
        admin.site.site_title = 'Gravel Calculator Pro'
        admin.site.index_title = 'Site Administration'
