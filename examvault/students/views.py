from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from questionbank.models import QuestionBank
from .models import StudentProfile


# ========================
# QUESTION BANK
# ========================
@login_required
def question_banks(request):

    banks = QuestionBank.objects.all()

    return render(request, "question_banks.html", {
        "banks": banks
    })


# ========================
# CONSULTANCY
# ========================
@login_required
def teacher_consultancy(request):
    return render(request, "teacher_consultancy.html")


# ========================
# STUDENT PROFILE (NEW 🔥)
# ========================
@login_required
def student_profile(request):

    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST.get('name')
        profile.phone = request.POST.get('phone')
        profile.institution = request.POST.get('institution')

        profile.class_name = request.POST.get('class')
        profile.date_of_birth = request.POST.get('dob')

        if request.FILES.get('image'):
            profile.image = request.FILES.get('image')

        if request.FILES.get('id_card'):
            profile.id_card = request.FILES.get('id_card')

        profile.save()
        return redirect('student_dashboard')

    return render(request, "student_profile.html", {"profile": profile})