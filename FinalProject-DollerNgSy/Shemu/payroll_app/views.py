from django.shortcuts import render

# Create your views here.

def test_page(request): # this is only to test the base. remove once completed
    return render(request, 'payroll_app/base.html')
