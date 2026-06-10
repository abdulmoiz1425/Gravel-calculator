from django.shortcuts import render
from .models import GravelType


def home(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'meta_title': 'Gravel Calculator Pro – Free Gravel Volume, Weight & Cost Calculator',
        'meta_description': 'Calculate exactly how much gravel you need for driveways, walkways, and landscaping. Free online gravel calculator with volume, weight, and cost estimation.',
    }
    return render(request, 'home.html', context)
