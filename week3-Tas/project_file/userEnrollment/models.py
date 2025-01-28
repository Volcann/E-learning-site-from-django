from django.db import models
from django.contrib.auth.models import User
from crudCoursesLectures.models import Course  # Assuming Course model is in `courses` app

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user enrolling in the course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # The course the user is enrolling in
    enrolled_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the user enrolled

    class Meta:
        unique_together = ('user', 'course')  # Ensuring a user can't enroll in the same course more than once

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"