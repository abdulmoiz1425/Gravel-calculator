from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.static import serve
from blog.sitemaps import BlogPostSitemap
from pages.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('calculator.urls')),
    path('', include('blog.urls')),
    path('', include('pages.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

handler404 = 'pages.views.custom_404'

# Serve user-uploaded media regardless of DEBUG, since this project has no
# separate web server (nginx/etc.) configured to serve /media/ in production.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
