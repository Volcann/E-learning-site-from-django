from rest_framework import generics, permissions
from .models import Course, Lecture
from .serializers import CourseSerializer, LectureSerializer
from .permissions import IsOwnerOrReadOnly

# List/Create Courses
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.prefetch_related('lectures').all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Retrieve/Update/Delete Course
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.prefetch_related('lectures').select_related('created_by').all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

# List/Create Lectures
class LectureListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.select_related('course').all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve/Update/Delete Lecture
class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.select_related('course').all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
