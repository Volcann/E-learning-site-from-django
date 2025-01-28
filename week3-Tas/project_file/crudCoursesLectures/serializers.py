from rest_framework import serializers
from .models import Course, Lecture

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'content', 'course', 'created_at']

class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'lectures']
        extra_kwargs = {
            'created_by': {'read_only': True},
        }
