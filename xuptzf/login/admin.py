from django.contrib import admin

# Register your models here.
from login.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'student_name', 'student_college', 'student_class']


admin.site.register(Student, StudentAdmin)
