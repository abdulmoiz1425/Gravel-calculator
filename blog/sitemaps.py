from django.contrib.sitemaps import Sitemap
from .models import BlogPost


class BlogPostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return BlogPost.objects.filter(status=BlogPost.STATUS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated_at
