from django.shortcuts import render

from .models import Course

def courses(request):
    ctx = {
        'courses': Course.objects.all()
    }
    return render(request, 'university/courses.html', ctx)
