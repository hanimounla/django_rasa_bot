from django.db import models

from user.models import Lecturer

class University(models.Model):
    name = models.CharField("University Name", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"


class Branche(models.Model):
    name = models.CharField("Branche", max_length=50)
    address = models.CharField("Address", max_length=150)
    university = models.ForeignKey(
        University, verbose_name="university", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branche"
        verbose_name_plural = "Branches"
        
        

class Faculty(models.Model):
    name = models.CharField("Faculty Name", max_length=50)
    open_date = models.DateField("Open Date", null=True, blank=True)
    branche = models.ForeignKey(
        Branche, verbose_name="branche", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class Course(models.Model):
    title = models.CharField("Course Title", max_length=50)
    total_hours = models.IntegerField("Total Course Hours")
    faculties = models.ManyToManyField(Faculty, related_name="faculty")
    prev_course = models.ForeignKey(
        "self",
        verbose_name="Previous Course",
        related_name="previous_course",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Class(models.Model):
    title = models.CharField("Class Title", max_length=50)
    class_date = models.DateField("Class Date", null=True, blank=True)
    branche = models.ForeignKey(
        Branche, verbose_name="branche", on_delete=models.SET_NULL, null=True
    )
    course = models.ForeignKey(
        Course, verbose_name="course", on_delete=models.SET_NULL, null=True
    )
    lecturer = models.ForeignKey(
        Lecturer, verbose_name="lecturer", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
