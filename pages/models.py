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


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.full_name} – {self.subject} ({self.created_at:%Y-%m-%d})'
