from django.test import TestCase

# Create your tests here.
from login import login_request

if __name__ == '__main__':
    print(login_request.response)
    login_request.login('04152017','woaini742','77gv','w3vjjz55z4yxor55qqcsypbw',)
    print(login_request.response)
