from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]