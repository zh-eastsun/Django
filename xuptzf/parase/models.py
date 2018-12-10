from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.CharField(max_length=8)
    student_name = models.CharField(max_length=30)
    student_sex = models.CharField(max_length=1)
    student_college = models.CharField(max_length=15)
    student_class = models.CharField(max_length=10)