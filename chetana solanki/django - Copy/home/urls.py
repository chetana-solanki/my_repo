from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('overview/', views.overview, name='overview'),
    path('board_of_directors/', views.board_of_directors, name='board_of_directors'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('cbse_mandatory_disclosure/', views.cbse_mandatory_disclosure, name='cbse_mandatory_disclosure'),
    path('academic/', views.academic, name='academic'),
    path('gallery/', views.gallery, name='gallery'),
    path('admissions/', views.admissions, name='admissions'),
    path('teacher/', views.teacher, name='teacher'),
    path('achievements/', views.achievements, name='achievements'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('student_registration/', views.student_registration, name='student_registration'),
    path('teacher_registration/', views.teacher_registration, name='teacher_registration'),
    path('worker_registration/', views.worker_registration, name='worker_registration'),
    path('pride_of_shanti_niketan/', views.pride_of_shanti_niketan, name='pride_of_shanti_niketan'),
    path('bus_rute_staff/', views.bus_rute_staff, name='bus_rute_staff'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('worker_dashboard/', views.worker_dashboard, name='worker_dashboard'),
    path('form/', views.form, name='form'),
    path('photo_gallery/', views.photo_gallery, name='photo_gallery'),
    path('video_gallery/', views.video_gallery, name='video_gallery'),
    
]