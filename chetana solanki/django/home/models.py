# d:\OneDrive\Desktop\chetana solanki\django - Copy\home\models.py

from django.db import models

# This line tells Django to create a database table named 'home_faculty'
class Faculty(models.Model):
    # A field to upload an image. It's optional.
    # 'upload_to' specifies that images will be saved in a 'faculty_pics' folder
    # inside your media directory.
    profile_picture = models.ImageField(upload_to='faculty_pics/', blank=True, null=True, verbose_name="Photo")
    
    # A required text field for the faculty's name, with a max length of 100 characters.
    name = models.CharField(max_length=100)
    
    # A required text field for the subject they teach.
    subject = models.CharField(max_length=100)
    
    # An optional field for age, storing a whole number.
    age = models.IntegerField(null=True, blank=True)
    
    # An optional field for experience, with helpful text for the admin panel.
    experience = models.IntegerField(null=True, blank=True, help_text="Experience in years")


    # This special method defines how a Faculty object should be displayed as a string.
    # For example, in the admin panel, you'll see the faculty's name instead of "Faculty object (1)".
    def __str__(self):
        return self.name
        # this will show comma seprated values, not a table
        # return f'{self.name}, {self.subject}, {self.age}, {self.experience}'



# Defines the data model for user registrations.
# This will create a database table named 'home_registration'.
class StudentRegistration(models.Model):
    # A unique identifier for each user, stored as text.
    # `unique=True` ensures no two users can have the same user_id.
    user_id = models.CharField(max_length=100, unique=True)
    
    # A field to store the user's full name.
    full_name = models.CharField(max_length=100)
    
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
    

class TeacherRegistration(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class WorkerRegistration(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
     





