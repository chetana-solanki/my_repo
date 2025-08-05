from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty # Step 1: Apne Faculty model ko import karein

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def admissions(request):
    return render(request, "admission.html")

def faculty(request):
    # Step 2: Database se saare faculty members ki list nikalein
    all_faculty = Faculty.objects.all()
    # Step 3: Is list ko ek 'context' dictionary mein daalein
    context = {'faculty_list': all_faculty}
    # Step 4: Context ko template ke saath render karein
    return render(request, "faculty.html", context)

def achievements(request):
    return render(request, "achievements.html")

def login(request):
    return render(request, "login.html")

def registration(request):
    return render(request, "registration.html")
