from django.shortcuts import render
from .models import GravelType


def home(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'meta_title': 'Gravel Calculator Pro – Free Gravel Volume, Weight & Cost Calculator',
        'meta_description': 'Use our free Gravel Calculator 2026 to estimate gravel tons, cubic yards, cubic feet, and cost for driveways, French drains, pavers, and home projects.',
    }
    return render(request, 'home.html', context)
