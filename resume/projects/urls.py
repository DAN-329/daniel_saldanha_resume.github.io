from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.pro,name='pro'),
    
]