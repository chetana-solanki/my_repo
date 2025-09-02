from django.contrib import admin
from .models import Teacher, StudentRegistration, WorkerRegistration, Enquiry

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'subject', 'age', 'experience', 'joined_date')


class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'mobile_number', 'email', 'joined_date')



class WorkerRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'mobile_number', 'email', 'joined_date')


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ( 'full_name', 'phone_number', 'email', 'class_name', 'joined_date')

# With the default registration, the list of faculty members in your admin panel will just show one column containing the output of the __str__ method, which is the faculty member's name. It's functional, but not very informative.
# admin.site.register(Faculty)

# Here, you've created a special class RegistrationAdmin that inherits from admin.ModelAdmin. This class acts as a configuration for the Registration model's admin page.
# The key part is list_display = ('user_id', 'full_name', 'email', 'joined_date'). This tells Django: "When you show the list of all registrations, don't just show the default __str__ value. Instead, create a table with columns for user_id, full_name, email, and joined_date."
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(StudentRegistration, StudentRegistrationAdmin)
admin.site.register(WorkerRegistration, WorkerRegistrationAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
