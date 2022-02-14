from django.db import models

# Shouldn't be able to delete the university
class University(models.Model):
    name = models.CharField("University Name", max_length=50)
    
    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"


class Faculty(models.Model):
    name = models.CharField("Faculty Name", max_length=50)
    open_date = models.DateField("Open Date", null=True, blank=True)
    university = models.ForeignKey(
        University, verbose_name="university", on_delete=models.SET_NULL, null=True
    )
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class Course(models.Model):
    title = models.CharField("Course Title", max_length=50)
    total_hours = models.IntegerField("Total Course Hours")
    prev_course = models.ForeignKey(
        "self",
        verbose_name="Previous Course",
        related_name="previous_course",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
