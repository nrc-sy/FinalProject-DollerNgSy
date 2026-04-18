from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_page, name='test'), # this is only to test the base. remove once completed
]