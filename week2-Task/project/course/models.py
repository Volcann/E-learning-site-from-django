from django.db import models
from django.contrib import admin

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in hours

    def __str__(self):
        return self.title

class Lecture(models.Model):
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.course.title}"