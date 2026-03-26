from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as acc_views
from dashboard import views as dash_views
from students import views as student_views
from teachers import views as teacher_views


urlpatterns = [

    # 🔥 HOME PAGE (IMPORTANT)
    path('', dash_views.home, name="home"),

    path('admin/', admin.site.urls),

    path('register/', acc_views.register_view, name='register'),
    path('login/', acc_views.login_view, name='login'),
    path('logout/', acc_views.logout_view, name='logout'),

    path('student/dashboard/', dash_views.student_dashboard, name="student_dashboard"),
    path('teacher/dashboard/', dash_views.teacher_dashboard, name="teacher_dashboard"),

    path('question-banks/', student_views.question_banks, name="question_banks"),

    path('add-question/', teacher_views.add_question, name="add_question"),

    path('exam/', include('exam.urls')),
    path('questionbank/', include('questionbank.urls')),
    path('teacher/', include('teachers.urls')),
    path('students/', include('students.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)