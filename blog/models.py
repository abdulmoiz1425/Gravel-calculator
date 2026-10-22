from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_UNPUBLISHED = 'unpublished'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_UNPUBLISHED, 'Unpublished'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.CharField(max_length=100, default='Gravel Calculator Pro')
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    excerpt = models.TextField(max_length=500, help_text='Short summary shown on listing page')
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    is_featured = models.BooleanField(default=False, help_text='Show as featured post on blog listing')
    publish_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField('SEO Title', max_length=70, blank=True)
    meta_description = models.CharField('Meta Description', max_length=300, blank=True)
    focus_keyword_title = models.CharField(
        'Focus Keyword in Title', max_length=100, blank=True,
        help_text='Checked against the SEO title'
    )
    focus_keyword_description = models.CharField(
        'Focus Keyword in Description', max_length=100, blank=True,
        help_text='Checked against the meta description'
    )
    reading_time = models.PositiveIntegerField(default=5, help_text='Estimated reading time in minutes')

    class Meta:
        ordering = ['-publish_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def get_related_posts(self):
        related = BlogPost.objects.filter(
            status=self.STATUS_PUBLISHED
        ).exclude(pk=self.pk)
        picked = []
        if self.category_id:
            picked = list(related.filter(category_id=self.category_id)[:3])
        if len(picked) < 3:
            seen = {p.pk for p in picked}
            by_tags = related.filter(tags__in=self.tags.all()).exclude(pk__in=seen).distinct()
            picked += list(by_tags[:3 - len(picked)])
        return picked
