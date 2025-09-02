from django.shortcuts import render,redirect
from .models import Teacher# Step 1: Apne Teacher model ko import karein
from .models import StudentRegistration, WorkerRegistration , Enquiry

# Create your views here.



def home(request):
    return render(request, "index.html")

def overview(request):
    return render(request, "overview.html")

def board_of_directors(request):
    return render(request, "board_of_directors.html")

def infrastructure(request):
    return render(request, "infrastructure.html")

def contact(request):
    return render(request, "contact.html")

def cbse_mandatory_disclosure(request):
    return render(request, "cbse_mandatory_disclosure.html")

def pride_of_shanti_niketan(request):
    return render(request, "pride_of_shanti_niketan.html")

def academic(request):
    return render(request, "academic.html")

def gallery(request):
    return render(request, "gallery.html")

def admissions(request):
    return render(request, "admission.html")

def bus_rute_staff(request):
    return render(request, "bus_rute_staff.html")

def teacher(request):
    # Step 2: Database se saare teacher members ki list nikalein
    all_teachers = Teacher.objects.all()
    # Step 3: Is list ko ek 'context' dictionary mein daalein
    context = {'teacher_list': all_teachers}
    # Step 4: Context ko template ke saath render karein
    return render(request, "teacher.html", context)

def achievements(request):
    return render(request, "achievements.html")

def student_dashboard(request):
    return render(request, "student_dashboard.html")

def teacher_dashboard(request):
    return render(request, "teacher_dashboard.html")

def worker_dashboard(request):
    return render(request, "worker_dashboard.html")

def photo_gallery(request):
    return render(request, "photo_gallery.html")

def video_gallery(request):
    return render(request, "video_gallery.html")

def login(request):
    error = ""
    if request.method == "POST":
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        student = StudentRegistration.objects.filter(user_id=user_id, password=password).first() 
        teacher = Teacher.objects.filter(user_id=user_id, password=password).first() 
        worker = WorkerRegistration.objects.filter(user_id=user_id, password=password).first()
        if student:
            return redirect(student_dashboard)
        elif teacher:
            return redirect(teacher_dashboard)
        elif worker:
            return redirect(worker_dashboard)
        else:
            error = "Invalid credentials"
    return render(request, "login.html", {"error": error})
    


def student_registration(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        full_name = request.POST.get("full_name")
        mobile_number = request.POST.get("mobile_number")      
        email = request.POST.get("email")
        password = request.POST.get("password")
        class_name = request.POST.get("class_name")
        # It immediately saves that instance to the database, creating a new row in the home_registration table
        StudentRegistration.objects.create(user_id=user_id, full_name=full_name, mobile_number=mobile_number, email=email, password=password, class_name=class_name)
        return redirect("login")

    return render(request, "student_registration.html")


def teacher_registration(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        full_name = request.POST.get("full_name")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        subject = request.POST.get("subject")
        age = request.POST.get("age")  # Added age field
        experience = request.POST.get("experience")  # Added experience field
        profile_picture = request.FILES.get("profile_picture")  # Handle file upload (optional)

        # Basic validation - removed mobile_number and email from required fields since they're optional in model
        # Added age and experience to required fields
        if not all([user_id, full_name, password]):
            # Handle validation error - you might want to add proper error handling
            return render(request, "teacher_registration.html", {"error": "All required fields must be filled"})

        try:
            # Convert age and experience to integers
            age = int(age)
            experience = int(experience)
        except ValueError:
            return render(request, "teacher_registration.html", {"error": "Age and experience must be valid numbers"})

        # Create new teacher using Teacher model
        Teacher.objects.create(
            user_id=user_id,
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            password=password,
            subject=subject,
            age=age,  # Added age field
            experience=experience,  # Added experience field
            profile_picture=profile_picture  # This is optional, so it can be None
        )
        return redirect("login")

    return render(request, "teacher_registration.html")

def worker_registration(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        full_name = request.POST.get("full_name")
        mobile_number = request.POST.get("mobile_number")      
        email = request.POST.get("email")
        password = request.POST.get("password")
        work_type = request.POST.get("work_type")   
        # It immediately saves that instance to the database, creating a new row in the home_registration table
        WorkerRegistration.objects.create(user_id=user_id, full_name=full_name, mobile_number=mobile_number, email=email, password=password, work_type=work_type)
        return redirect("login")

    return render(request, "worker_registration.html")


def form(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")      
        email = request.POST.get("email")
        message = request.POST.get("message")   
        class_name = request.POST.get("class_name") 
        Enquiry.objects.create(full_name=full_name, phone_number=phone_number, email=email, message=message, class_name=class_name)
        return redirect("form")
    return render(request, "form.html")