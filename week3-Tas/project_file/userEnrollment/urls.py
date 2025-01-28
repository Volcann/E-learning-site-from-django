from django.urls import path
from .views import EnrollmentListView, EnrollmentDetailView

urlpatterns = [
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list_create'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
]
