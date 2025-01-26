from django.contrib import admin
from .models import SuccessMetric, SuccessStory

# Registering the models
admin.site.register(SuccessStory)
admin.site.register(SuccessMetric)