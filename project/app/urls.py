from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for API endpoints
    path('', views.home, name='home'),
    path('api/question/<int:id>/', views.api_question, name='api_question'),
    path('api/check_score/', views.check_score, name='check_score'),
    path('api/courses/', views.get_courses, name='get_courses'),  
]
