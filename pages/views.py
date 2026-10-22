from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.shortcuts import redirect, render

from .models import ContactMessage

CONTACT_SUBJECTS = {
    'calculator-question': 'Question about the gravel calculator',
    'estimate-error': 'Error in volume, weight, or cost estimate',
    'suggestion': 'Suggestion for a new calculator or guide',
    'content-issue': 'Incorrect or outdated website content',
    'privacy-legal': 'Privacy, cookie, or copyright concern',
    'business': 'Advertising, partnership, or business inquiry',
    'other': 'Other',
}


def about(request):
    context = {
        'meta_title': 'About GravelYardCalculator.com',
        'meta_description': 'Learn what GravelYardCalculator.com helps estimate, how gravel calculations work, and why supplier specifications matter.',
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('message', '').strip()
        error = None
        if not name or len(name) > 120:
            error = 'Please enter your full name.'
        elif subject not in CONTACT_SUBJECTS:
            error = 'Please select a subject.'
        elif not body or len(body) > 5000:
            error = 'Please enter a message (up to 5,000 characters).'
        else:
            try:
                validate_email(email)
            except ValidationError:
                error = 'Please enter a valid email address.'
        if error:
            messages.error(request, error)
            return redirect('contact')
        msg = ContactMessage.objects.create(
            full_name=name, email=email, subject=subject, message=body)
        if settings.CONTACT_NOTIFY_EMAIL:
            try:
                send_mail(
                    f'[Contact] {CONTACT_SUBJECTS[subject]}',
                    f'From: {name} <{email}>\n\n{body}',
                    None, [settings.CONTACT_NOTIFY_EMAIL], fail_silently=True)
            except Exception:
                pass  # the message is already saved; email is best-effort
        messages.success(request, 'Thank you. Your message has been received.')
        return redirect('contact')

    context = {
        'meta_title': 'Contact GravelYardCalculator.com',
        'meta_description': 'Contact GravelYardCalculator.com about calculator issues, website feedback, or questions about the information provided.',
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
