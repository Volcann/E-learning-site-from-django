from course.models import Course, Lecture
from django import forms

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'content', 'date']