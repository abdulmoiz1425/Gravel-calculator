from django.db import models
from ckeditor.fields import RichTextField


class PageContent(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
        ('privacy', 'Privacy Policy'),
    ]
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    content = RichTextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Page Content'
        verbose_name_plural = 'Page Contents'

    def __str__(self):
        return f'{self.get_page_display()} Content'
