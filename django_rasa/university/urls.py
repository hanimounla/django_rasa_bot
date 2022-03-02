from django.urls import path
from . import views

app_name="university"

urlpatterns = [
    path('courses/', views.courses, name='courses'),
]