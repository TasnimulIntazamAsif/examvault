from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from questionbank.models import QuestionBank, Question
from exam.models import Exam
from .models import TeacherProfile


# ========================
# CREATE EXAM (FIXED ✅)
# ========================
@login_required
def create_exam(request):

    banks = QuestionBank.objects.all()

    # 👉 selected bank
    selected_bank_id = request.GET.get('bank')

    # 👉 default empty queryset
    questions = Question.objects.none()

    # 👉 filter questions
    if selected_bank_id:
        questions = Question.objects.filter(bank_id=selected_bank_id)

    if request.method == "POST":
        title = request.POST.get("title")
        selected_questions = request.POST.getlist("questions")

        # ❗ safety check
        if not selected_questions:
            return render(request, "create_exam.html", {
                "questions": questions,
                "banks": banks,
                "error": "Select at least one question"
            })

        # ✅ FIXED (removed teacher + is_published)
        exam = Exam.objects.create(
            title=title,
            total_questions=len(selected_questions),
            question_bank_id=selected_bank_id if selected_bank_id else None
        )

        # 👉 add selected questions
        exam.questions.set(selected_questions)

        return redirect("teacher_exam_list")

    return render(request, "create_exam.html", {
        "questions": questions,
        "banks": banks,
        "selected_bank": selected_bank_id
    })


# ========================
# ADD QUESTION
# ========================
@login_required
def add_question(request):

    banks = QuestionBank.objects.all()

    if request.method == "POST":

        Question.objects.create(
            bank_id=request.POST.get("bank"),
            question_text=request.POST.get("question"),

            option_a=request.POST.get("a"),
            option_b=request.POST.get("b"),
            option_c=request.POST.get("c"),
            option_d=request.POST.get("d"),

            correct_option=request.POST.get("correct"),
            explanation=request.POST.get("explanation")
        )

        return redirect("teacher_dashboard")

    return render(request, "add_question.html", {"banks": banks})


# ========================
# TEACHER PROFILE
# ========================
@login_required
def teacher_profile(request):

    profile, created = TeacherProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST.get('name')
        profile.phone = request.POST.get('phone')
        profile.institution = request.POST.get('institution')

        profile.subject = request.POST.get('subject')
        profile.experience = request.POST.get('experience')
        profile.date_of_birth = request.POST.get('dob')

        if request.FILES.get('image'):
            profile.image = request.FILES.get('image')

        if request.FILES.get('id_card'):
            profile.id_card = request.FILES.get('id_card')

        profile.save()
        return redirect('teacher_dashboard')

    return render(request, "teacher_profile.html", {"profile": profile})