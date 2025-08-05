from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def staff(request):
    return render(request, 'staff.html')
def students(request):
    return render(request, 'students.html')
def teachers(request):
    return render(request, 'teachers.html')