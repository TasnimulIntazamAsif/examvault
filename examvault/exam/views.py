from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exam, ExamAttempt, Answer


# ========================
# EXAM LIST (IMPORTANT)
# ========================
@login_required
def exam_list(request):

    exams = Exam.objects.all()

    return render(request, "exam_list.html", {
        "exams": exams
    })


# ========================
# START EXAM
# ========================
@login_required
def start_exam(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    # 🔥 Use admin selected questions
    questions = exam.questions.all()

    attempt = ExamAttempt.objects.create(
        student=request.user,
        exam=exam,
        total_questions=questions.count()
    )

    attempt.questions.set(questions)

    return render(request, "exam_page.html", {
        "exam": exam,
        "questions": questions,
        "attempt": attempt
    })


# ========================
# SUBMIT EXAM
# ========================
@login_required
def submit_exam(request, attempt_id):

    attempt = get_object_or_404(ExamAttempt, id=attempt_id)

    questions = attempt.questions.all()

    correct = 0
    wrong = 0
    unanswered = 0

    for q in questions:

        selected = request.POST.get(str(q.id))

        if not selected:
            unanswered += 1
            is_correct = False

        elif selected == q.correct_option:
            correct += 1
            is_correct = True

        else:
            wrong += 1
            is_correct = False

        Answer.objects.create(
            attempt=attempt,
            question=q,
            selected_option=selected if selected else "",
            is_correct=is_correct
        )

    attempt.correct = correct
    attempt.wrong = wrong
    attempt.unanswered = unanswered
    attempt.score = correct
    attempt.save()

    return redirect("exam_result", attempt_id=attempt.id)


# ========================
# RESULT
# ========================
@login_required
def exam_result(request, attempt_id):

    attempt = get_object_or_404(ExamAttempt, id=attempt_id)

    answers = Answer.objects.filter(attempt=attempt)

    return render(request, "exam_result.html", {
        "attempt": attempt,
        "answers": answers
    })