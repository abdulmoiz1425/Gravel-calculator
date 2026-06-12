from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    ITEMS = {
        'home': {'priority': 1.0, 'changefreq': 'weekly'},
        'about': {'priority': 0.7, 'changefreq': 'monthly'},
        'blog:list': {'priority': 0.8, 'changefreq': 'weekly'},
        'contact': {'priority': 0.5, 'changefreq': 'monthly'},
        'privacy': {'priority': 0.3, 'changefreq': 'yearly'},
        'cookie_policy': {'priority': 0.3, 'changefreq': 'yearly'},
        'disclaimer': {'priority': 0.3, 'changefreq': 'yearly'},
        'terms': {'priority': 0.3, 'changefreq': 'yearly'},
    }

    def items(self):
        return list(self.ITEMS.keys())

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return self.ITEMS[item]['priority']

    def changefreq(self, item):
        return self.ITEMS[item]['changefreq']
