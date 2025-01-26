# models.py
from django.db import models
    
class SuccessMetric(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='metrics/')

    def __str__(self):
        return self.title

class SuccessStory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='stories/')

    def __str__(self):
        return self.title
