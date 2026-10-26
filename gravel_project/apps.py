from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    def ready(self):
        super().ready()
        from django.contrib import admin
        admin.site.site_header = 'GravelYardCalculator.com Admin'
        admin.site.site_title = 'GravelYardCalculator.com'
        admin.site.index_title = 'Site Administration'
