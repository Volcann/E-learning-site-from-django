from rest_framework import generics, permissions
from .models import Enrollment
from .serializers import EnrollmentSerializer
from crudCoursesLectures.models import Course  # Assuming Course model is in the courses app
from rest_framework.permissions import IsAuthenticated

class EnrollmentListView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can enroll or view enrollments

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        course = Course.objects.get(id=course_id)
        user = self.request.user  # Current authenticated user
        serializer.save(user=user, course=course)

class EnrollmentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]