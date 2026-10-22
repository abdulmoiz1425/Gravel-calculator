from django.shortcuts import render
from .models import GravelType


def home(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'meta_title': 'Gravel Calculator — Estimate Gravel, Tons, Yards & Cost',
        'meta_description': 'Calculate gravel volume, cubic yards, estimated tons, and material cost for driveways, patios, paths, and landscaping projects.',
    }
    return render(request, 'home.html', context)


def driveway_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Crushed Stone',
        'meta_title': 'Driveway Gravel Calculator — Estimate Yards, Tons & Cost',
        'meta_description': 'Calculate driveway gravel volume and estimate weight and cost. Check dimensions, layer depth, and supplier pricing before ordering.',
    }
    return render(request, 'driveway_calculator.html', context)


def pea_gravel_calculator(request):
    context = {
        'meta_title': 'Pea Gravel Calculator — Yards, Tons, Bags & Cost',
        'meta_description': 'Estimate pea gravel volume, weight, bags, and material cost for patios, paths, and landscape areas.',
    }
    return render(request, 'pea_gravel_calculator.html', context)


def french_drain_calculator(request):
    context = {
        'meta_title': 'French Drain Gravel Calculator — Yards, Tons & Cost',
        'meta_description': 'Estimate drainage stone for a French drain trench in cubic yards and tons. Subtracts pipe volume and shows a suggested order with a 10% allowance.',
    }
    return render(request, 'french_drain_calculator.html', context)


def landscaping_gravel_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Pea Gravel',
        'meta_title': 'Landscaping Gravel Calculator — Yards, Tons & Cost',
        'meta_description': 'Estimate gravel for garden beds, landscape borders, and paths. Calculate volume and review material assumptions before ordering.',
    }
    return render(request, 'landscaping_gravel_calculator.html', context)


def crushed_gravel_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Crushed Stone',
        'meta_title': 'Crushed Gravel Calculator — Yards, Tons & Cost',
        'meta_description': 'Estimate crushed gravel volume, weight, and material cost for paths, driveways, and base projects.',
    }
    return render(request, 'crushed_gravel_calculator.html', context)
