from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER_CHOICES = [
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    
    HUMAN_RESOURCES = "HR"
    TESTER = "TE"
    SOFTWARE_DEV= "SD"
    
    JOB_CHOICES = [
        (HUMAN_RESOURCES, 'HR'),
        (SOFTWARE_DEV, 'Software Dev'),
        (TESTER, 'Tester'),
    ]
    job_category = models.CharField(max_length=2, choices=JOB_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"