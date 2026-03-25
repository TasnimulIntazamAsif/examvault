from django.urls import path
from .views import teacher_consultancy, question_banks, student_profile

urlpatterns = [
    path('consultancy/', teacher_consultancy, name='teacher_consultancy'),
    path('question-banks/', question_banks, name='question_banks'),
    path('profile/', student_profile, name='student_profile'),
]