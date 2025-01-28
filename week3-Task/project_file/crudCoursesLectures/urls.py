from django.urls import path

from .views import (
    CourseListCreateView,
    CourseDetailView,
    LectureListCreateView,
    LectureDetailView,
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course_list_create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('lectures/', LectureListCreateView.as_view(), name='lecture_list_create'),
    path('lectures/<int:pk>/', LectureDetailView.as_view(), name='lecture_detail'),
]
