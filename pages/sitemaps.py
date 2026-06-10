from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'blog:list', 'contact', 'privacy']

    def location(self, item):
        return reverse(item)
