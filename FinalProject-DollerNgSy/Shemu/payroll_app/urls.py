from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.test_page, name='test'),  # temporary; ill remove soon
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/update/<int:pk>/', views.update_employee, name='update_employee'),
]








'''
Reference(s):
- https://docs.djangoproject.com/en/6.0/topics/auth/default/
'''

