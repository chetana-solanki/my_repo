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
