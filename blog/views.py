from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, Category, Tag


def blog_list(request):
    posts = BlogPost.objects.filter(status=BlogPost.STATUS_PUBLISHED)
    featured = posts.filter(is_featured=True).first()
    regular_posts = posts.exclude(pk=featured.pk) if featured else posts

    paginator = Paginator(regular_posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'featured': featured,
        'page_obj': page_obj,
        'total_count': posts.count(),
        'meta_title': 'Construction & Gravel Blog – Expert Articles | Gravel Calculator Pro',
        'meta_description': 'Expert articles on gravel selection, driveway installation, drainage, cost management, and landscaping tips from Gravel Calculator Pro.',
    }
    return render(request, 'blog/list.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status=BlogPost.STATUS_PUBLISHED)
    related_posts = post.get_related_posts()

    context = {
        'post': post,
        'related_posts': related_posts,
        'meta_title': post.meta_title or post.title,
        'meta_description': post.meta_description or post.excerpt,
    }
    return render(request, 'blog/detail.html', context)
