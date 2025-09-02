# d:\OneDrive\Desktop\chetana solanki\django - Copy\home\models.py

from django.db import models

# This line tells Django to create a database table named 'home_teacher'
class Teacher(models.Model):
    # Registration fields
    user_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=100)

    # A field to upload an image. It's optional.
    # 'upload_to' specifies that images will be saved in a 'teachers' folder
    # inside your media directory.
    profile_picture = models.ImageField(upload_to='teachers/', blank=True, null=True, verbose_name="Photo")

    # A required text field for the subject they teach.
    subject = models.CharField(max_length=100, null=True, blank=True)

    # An optional field for age, storing a whole number.
    age = models.IntegerField(null=True, blank=True)

    # An optional field for experience, with helpful text for the admin panel.
    experience = models.IntegerField(null=True, blank=True)

    # Auto-generated timestamp when teacher registers
    joined_date = models.DateTimeField(auto_now_add=True)


    # This special method defines how a Teacher object should be displayed as a string.
    # For example, in the admin panel, you'll see the teacher's name instead of "Teacher object (1)".
    def __str__(self):
        return self.full_name
        # this will show comma seprated values, not a table
        # return f'{self.full_name}, {self.subject}, {self.age}, {self.experience}'



# Defines the data model for user registrations.
# This will create a database table named 'home_registration'.
class StudentRegistration(models.Model):
    # A unique identifier for each user, stored as text.
    # `unique=True` ensures no two users can have the same user_id.
    user_id = models.CharField(max_length=100, unique=True)
    
    # A field to store the user's full name.
    full_name = models.CharField(max_length=100)

    mobile_number = models.CharField(max_length=15)
    
    # A field for the user's email address.
    # `EmailField` provides basic email format validation.
    # `unique=True` ensures every user has a distinct email.
    email = models.EmailField(unique=True)
    
    # This field stores the password as PLAIN TEXT.
    password = models.CharField(max_length=100)
    
    class_name = models.CharField(max_length=100)
    # A field to automatically record the date and time when a user registers.
    # `auto_now_add=True` sets this value only once when the record is first created.
    joined_date = models.DateTimeField(auto_now_add=True)

    # Defines the string representation of a Registration object.
    # This is what you'll see in the Django admin panel or when you print the object.
    def __str__(self):
        return self.full_name
    



class WorkerRegistration(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Enquiry(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)    
    email = models.EmailField(unique=True)
    message = models.TextField()
    class_name = models.CharField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name     

