"""
URL configuration for examvault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#urlpatterns = [
    #path('admin/', admin.site.urls),
#]

from django.contrib import admin
from django.urls import path
from accounts import views as acc_views
from dashboard import views as dash_views

from students import views as student_views
from teachers import views as teacher_views
from dashboard import views as dash_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('register/', acc_views.register_view, name='register'),
    path('login/', acc_views.login_view, name='login'),
    path('logout/', acc_views.logout_view, name='logout'),

    #path('student/dashboard/', dash_views.student_dashboard, name='student_dashboard'),
    #path('teacher/dashboard/', dash_views.teacher_dashboard, name='teacher_dashboard'),
    #path('admin/dashboard/', dash_views.admin_dashboard, name='admin_dashboard'),
    
    path('student/dashboard/',dash_views.student_dashboard,name="student_dashboard"),

    path('teacher/dashboard/',dash_views.teacher_dashboard,name="teacher_dashboard"),

    path('question-banks/',student_views.question_banks,name="question_banks"),

    path('add-question/',teacher_views.add_question,name="add_question"),


]







