from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from parase.models import Student


def get_user_info(request):
    student_number = request.GET['stuNum']
    return HttpResponse(Student.objects.get(student_number=student_number))
