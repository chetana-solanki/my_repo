from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Faculty# Step 1: Apne Faculty model ko import karein
from .models import StudentRegistration, TeacherRegistration, WorkerRegistration

# Create your views here.



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
    error = ""
    if request.method == "POST":
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        user = StudentRegistration.objects.filter(user_id=user_id, password=password).first()
        if user:
            return render(request, "index.html", {"user": user})
        else:
            error = "Invalid credentials"
    return render(request, "login.html", {"error": error})
    


def student_registration(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        class_name = request.POST.get("class_name")
        # It immediately saves that instance to the database, creating a new row in the home_registration table
        StudentRegistration.objects.create(user_id=user_id, full_name=full_name, email=email, password=password, class_name=class_name)
        return redirect("login")

    return render(request, "student_registration.html")


def teacher_registration(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        subject = request.POST.get("subject")
        # It immediately saves that instance to the database, creating a new row in the home_registration table
        TeacherRegistration.objects.create(user_id=user_id, full_name=full_name, email=email, password=password, subject=subject)
        return redirect("login")

    return render(request, "teacher_registration.html")

def worker_registration(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        work_type = request.POST.get("work_type")
        # It immediately saves that instance to the database, creating a new row in the home_registration table
        WorkerRegistration.objects.create(user_id=user_id, full_name=full_name, email=email, password=password, work_type=work_type)
        return redirect("login")

    return render(request, "worker_registration.html")