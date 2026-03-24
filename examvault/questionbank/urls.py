from django.urls import path
from . import views

urlpatterns = [

    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('', views.question_bank_list, name='bank_list'),
    path('bank/<int:bank_id>/', views.view_questions, name='view_questions'),

]