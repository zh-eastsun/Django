from django.http import HttpResponse
from django.views.decorators.http import require_POST

from login import login_request, models


# Create your views here.


@require_POST
def login(request):
    stuNum = request.GET['stuNum']
    password = request.GET['password']
    checkcode = request.GET['checkcode']
    cookie = request.GET['cookie']

