from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/update/', views.course_update, name='course_update'),
    path('course/<int:course_id>/delete/', views.course_delete, name='course_delete'),
    path('lecture/create/<int:course_id>/', views.lecture_create, name='lecture_create'),
    path('lecture/<int:lecture_id>/update/', views.lecture_update, name='lecture_update'),
    path('lecture/<int:lecture_id>/delete/', views.lecture_delete, name='lecture_delete'),
]