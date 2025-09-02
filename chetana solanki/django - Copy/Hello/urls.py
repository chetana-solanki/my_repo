"""
URL configuration for Hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]

# Serve media files during development
# This code allows Django to serve user-uploaded files (like faculty photos) during development
# MEDIA_URL = '/media/' - URL prefix for media files in browser
# MEDIA_ROOT = 'media/' folder path - Physical location where files are stored
# Example: Browser requests /media/teachers/photo.jpg -> Django serves from media/teachers/photo.jpg
# NOTE: This only works when DEBUG=True (development mode)
# In production (DEBUG=False), web server (Nginx/Apache) handles media file serving
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
