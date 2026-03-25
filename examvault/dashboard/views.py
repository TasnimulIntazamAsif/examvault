from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import StudentProfile
from teachers.models import TeacherProfile


# ========================
# STUDENT DASHBOARD
# ========================
@login_required
def student_dashboard(request):

    profile = StudentProfile.objects.filter(user=request.user).first()

    return render(request, 'student_dashboard.html', {
        "profile": profile
    })


# ========================
# TEACHER DASHBOARD
# ========================
@login_required
def teacher_dashboard(request):

    profile = TeacherProfile.objects.filter(user=request.user).first()

    return render(request, 'teacher_dashboard.html', {
        "profile": profile
    })


# ========================
# ADMIN DASHBOARD
# ========================
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')