import email
from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    MALE, FEMALE = "m", "f"
    GENDER_OPTIONS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    
    id = models.IntegerField("Student ID", primary_key=True)
    first_name = models.CharField("First Name", max_length=50)
    father_name = models.CharField("Father Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    phone = models.CharField("Phone Number", max_length=15, null=True)
    email = models.EmailField("Email", null=True, blank=True)
    gender = models.CharField("Gender", choices=GENDER_OPTIONS, max_length=10, default=MALE)
    address = models.CharField("Address", max_length=100, null=True, blank=True)
    certificate_date = models.DateField("Certificate Date", null=True, blank=True)
    birth_date = models.DateField("Birth Date", null=True, blank=True)
    
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
