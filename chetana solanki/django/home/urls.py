from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admissions/', views.admissions, name='admissions'),
    path('faculty/', views.faculty, name='faculty'),
    path('achievements/', views.achievements, name='achievements'),
    path('login/', views.login, name='login'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('teacher_registration/', views.teacher_registration, name='teacher_registration'),
    path('worker_registration/', views.worker_registration, name='worker_registration'),
]