from django.shortcuts import render


def about(request):
    context = {
        'meta_title': 'About Gravel Calculator Pro – Free Online Gravel Calculator',
        'meta_description': 'Learn about Gravel Calculator Pro, our mission, and why we built the most accurate free online gravel calculator for contractors and homeowners.',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'meta_title': 'Contact Gravel Calculator Pro – Get in Touch',
        'meta_description': 'Contact the Gravel Calculator Pro team. We typically respond within 24 hours.',
    }
    return render(request, 'contact.html', context)


def privacy(request):
    context = {
        'meta_title': 'Privacy Policy – Gravel Calculator Pro',
        'meta_description': 'Read the Gravel Calculator Pro privacy policy. Learn how we protect your data and what information we collect.',
    }
    return render(request, 'privacy.html', context)


def disclaimer(request):
    context = {
        'meta_title': 'Disclaimer – Gravel Calculator Pro',
        'meta_description': 'Read the Gravel Calculator Pro disclaimer. Gravel calculations are estimates only. Always verify quantities with your supplier before purchasing.',
    }
    return render(request, 'disclaimer.html', context)


def cookie_policy(request):
    context = {
        'meta_title': 'Cookie Policy – Gravel Calculator Pro',
        'meta_description': 'Learn how Gravel Calculator Pro uses cookies and similar technologies to improve your experience.',
    }
    return render(request, 'cookie_policy.html', context)


def terms(request):
    context = {
        'meta_title': 'Terms and Conditions – Gravel Calculator Pro',
        'meta_description': 'Read the Terms and Conditions for using Gravel Calculator Pro. By using our calculator you agree to these terms.',
    }
    return render(request, 'terms.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
