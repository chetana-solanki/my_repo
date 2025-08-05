from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Home page view
    path('staff/', views.staff, name='staff'),  # Staff page view
    path('students/', views.students, name='students'),  # Students page view
    path('teachers/', views.teachers, name='teachers'),  # Teachers page view
]