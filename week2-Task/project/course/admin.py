from django.contrib import admin
from .models import Course, Lecture

# Registering the models
admin.site.register(Course)
admin.site.register(Lecture)
