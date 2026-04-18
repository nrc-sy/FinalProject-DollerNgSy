from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def test_page(request): # this is only to test the base. remove once completed
    return render(request, 'payroll_app/base.html')

@login_required(login_url='login')
def employee_list(request):
    return render(request, 'payroll_app/employees.html') # will update code tom
