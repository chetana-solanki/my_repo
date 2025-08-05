from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def admissions(request):
    return render(request, "admission.html")

def faculty(request):
    return render(request, "faculty.html")

def achievements(request):
    return render(request, "achievements.html")
