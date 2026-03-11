from django.urls import path
from . import views

urlpatterns = [

    path('', views.exam_list, name='exam_list'),

    path('start/<int:exam_id>/', views.start_exam, name='start_exam'),

    path('submit/<int:attempt_id>/', views.submit_exam, name='submit_exam'),

    path('result/<int:attempt_id>/', views.exam_result, name='exam_result'),

    path('teacher/exams/', views.teacher_exam_list, name='teacher_exam_list'),

]