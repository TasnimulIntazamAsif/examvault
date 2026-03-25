from django.urls import path
from .views import create_exam, add_question, teacher_profile

urlpatterns = [
    path('create-exam/', create_exam, name='create_exam'),
    path('add-question/', add_question, name='add_question'),
    path('profile/', teacher_profile, name='teacher_profile'),
]