from django.contrib import admin

from .models import *

class StudntDegreeAdmin(admin.ModelAdmin):
    list_filter = ("course", "degree")
    
    
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Branche)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(StudentDegree, StudntDegreeAdmin)
