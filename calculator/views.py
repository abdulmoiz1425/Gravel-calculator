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
        'meta_title': 'Driveway Gravel Calculator: Tons, Yards & Cost',
        'meta_description': 'Calculate driveway gravel in cubic yards and tons, estimate material cost, and plan your order using driveway dimensions and gravel depth.',
    }
    return render(request, 'driveway_calculator.html', context)


def pea_gravel_calculator(request):
    context = {
        'meta_title': 'Pea Gravel Calculator: Yards, Tons, Bags & Cost',
        'meta_description': 'Calculate pea gravel for garden beds, paths, patios, and landscaping. Estimate volume, weight, bags, and material cost from your measurements.',
    }
    return render(request, 'pea_gravel_calculator.html', context)


def french_drain_calculator(request):
    context = {
        'meta_title': 'French Drain Gravel Calculator: Yards, Tons & Cost',
        'meta_description': 'Estimate gravel for a French drain using trench dimensions and pipe diameter. Calculate drainage stone volume, approximate weight, and material cost.',
    }
    return render(request, 'french_drain_calculator.html', context)


def landscaping_gravel_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Pea Gravel',
        'meta_title': 'Landscaping Gravel Calculator: Yards, Tons & Cost',
        'meta_description': 'Estimate landscaping gravel for garden beds, paths, borders, and patios. Calculate material volume, approximate weight, and cost from your measurements.',
    }
    return render(request, 'landscaping_gravel_calculator.html', context)


def crushed_gravel_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Crushed Stone',
        'meta_title': 'Crushed Gravel Calculator: Yards, Tons & Cost',
        'meta_description': 'Estimate crushed gravel for driveways, paths, and base layers. Calculate cubic yards, approximate tons, and material cost using project dimensions.',
    }
    return render(request, 'crushed_gravel_calculator.html', context)
