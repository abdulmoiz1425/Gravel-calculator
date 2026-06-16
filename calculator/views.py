from django.shortcuts import render
from .models import GravelType


def home(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'meta_title': 'Free Gravel Calculator 2026 – Estimate Tons, Yards & Cost',
        'meta_description': 'Use our free Gravel Calculator 2026 to estimate gravel tons, cubic yards, cubic feet, and cost for driveways, French drains, pavers, and home projects.',
    }
    return render(request, 'home.html', context)
