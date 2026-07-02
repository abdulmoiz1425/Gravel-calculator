from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driveway-gravel-calculator/', views.driveway_calculator, name='driveway_calculator'),
    path('pea-gravel-calculator/', views.pea_gravel_calculator, name='pea_gravel_calculator'),
    path('french-drain-gravel-calculator/', views.french_drain_calculator, name='french_drain_calculator'),
    path('crushed-gravel-calculator/', views.crushed_gravel_calculator, name='crushed_gravel_calculator'),
    path('landscaping-gravel-calculator/', views.landscaping_gravel_calculator, name='landscaping_gravel_calculator'),
]
