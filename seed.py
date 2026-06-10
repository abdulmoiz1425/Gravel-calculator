"""
Run with: python3 seed.py
Seeds default gravel types and creates a superuser (admin / admin123).
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gravel_project.settings')
django.setup()

from calculator.models import GravelType
from django.contrib.auth.models import User

# Gravel types from SRS Section 11.3
GRAVEL_TYPES = [
    {'name': 'Pea Gravel',     'density': 1.6, 'typical_use': 'Small, rounded stones for walkways and drainage.',          'order': 1},
    {'name': 'Crushed Stone',  'density': 1.8, 'typical_use': 'Angular stones for driveways and foundations.',              'order': 2},
    {'name': 'River Rock',     'density': 1.5, 'typical_use': 'Smooth, decorative stones for landscaping.',                 'order': 3},
    {'name': 'Limestone',      'density': 1.7, 'typical_use': 'Durable stone for construction and road base.',              'order': 4},
    {'name': 'Granite',        'density': 1.9, 'typical_use': 'Heavy, hard stone for driveways and base layers.',           'order': 5},
    {'name': 'Sandstone',      'density': 1.6, 'typical_use': 'Decorative stone for patios and pathways.',                  'order': 6},
    {'name': 'Quartzite',      'density': 1.8, 'typical_use': 'Hard, decorative stone for landscaping.',                    'order': 7},
    {'name': 'Slate Chips',    'density': 1.7, 'typical_use': 'Decorative dark chips for gardens and borders.',             'order': 8},
]

print('Seeding gravel types...')
for g in GRAVEL_TYPES:
    obj, created = GravelType.objects.update_or_create(
        name=g['name'],
        defaults={'density': g['density'], 'typical_use': g['typical_use'], 'order': g['order'], 'is_active': True}
    )
    print(f'  {"Created" if created else "Updated"}: {obj.name}')

print('\nCreating superuser (username: admin, password: admin123)...')
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gravelcalculator.pro', 'admin123')
    print('  Superuser created.')
else:
    print('  Superuser already exists.')

print('\nDone! Start the server with: python3 manage.py runserver')
