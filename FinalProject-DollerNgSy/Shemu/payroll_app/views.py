# Tashannah Doller, ; Gide Ng, ; Nathan Riley Sy, 244311
# April , 2026

'''
I hereby attest to the truth of the following facts:

I have not discussed the Python language code in my program with anyone
other than my instructor or the teaching assistants assigned to this course.

I have not used Python language code obtained from another student, or
any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in my program was
obtained from another source, such as a textbook or course notes, that has been clearly noted with proper citation in the
comments of my program.
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def test_page(request): # this is only to test the base. remove once completed
    return render(request, 'payroll_app/base.html')

@login_required(login_url='login')
def employee_list(request):
    return render(request, 'payroll_app/employees.html') # will update code tom

def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_page')  # assumes you have an employees list view
    else:
        form = EmployeeForm()
    return render(request, 'payroll_app/create_employee.html', {'form': form})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_page')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'payroll_app/update_employee.html', {'form': form, 'employee': employee})
