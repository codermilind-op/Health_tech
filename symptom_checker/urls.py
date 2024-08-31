from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.symptom_checker, name='symptom_checker'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),     # Update if you have a profile view
    path('', views.symptom_checker, name='symptom_checker'),  # Example path
]
