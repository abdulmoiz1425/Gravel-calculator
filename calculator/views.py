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


def driveway_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Crushed Stone',
        'meta_title': 'Driveway Gravel Calculator – Estimate Tons, Yards & Cost',
        'meta_description': 'Use our free driveway gravel calculator to estimate cubic yards, tons, and cost for your gravel driveway. Enter length, width, depth, and gravel type for instant results.',
    }
    return render(request, 'driveway_calculator.html', context)


def pea_gravel_calculator(request):
    context = {
        'meta_title': 'Pea Gravel Calculator – Tons, Yards, Bags & Cost',
        'meta_description': 'Use our free pea gravel calculator to estimate cubic feet, cubic yards, tons, bags, and cost for patios, walkways, playgrounds, and driveways. Instant results.',
    }
    return render(request, 'pea_gravel_calculator.html', context)


def french_drain_calculator(request):
    context = {
        'meta_title': 'French Drain Gravel Calculator – Estimate Yards and Tons',
        'meta_description': 'Use our free French drain gravel calculator to estimate cubic feet, cubic yards, and tons of drainage stone. Subtracts pipe volume and adds a waste buffer for an accurate order estimate.',
    }
    return render(request, 'french_drain_calculator.html', context)


def landscaping_gravel_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Pea Gravel',
        'meta_title': 'Landscaping Gravel Calculator – Estimate Yards, Tons & Cost',
        'meta_description': 'Use our free landscaping gravel calculator to estimate cubic yards, tons, and cost for garden beds, paths, borders, patios, and decorative stone areas. Supports multiple shapes and gravel types.',
    }
    return render(request, 'landscaping_gravel_calculator.html', context)


def crushed_gravel_calculator(request):
    gravel_types = GravelType.objects.filter(is_active=True)
    context = {
        'gravel_types': gravel_types,
        'default_gravel_name': 'Crushed Stone',
        'meta_title': 'Crushed Gravel Calculator – Estimate Yards, Tons & Cost',
        'meta_description': 'Use our free crushed gravel calculator to estimate cubic yards, tons, and cost for driveways, walkways, patio bases, and drainage projects. Supports crusher run, 3/4 gravel, crusher fines, and crushed granite.',
    }
    return render(request, 'crushed_gravel_calculator.html', context)
