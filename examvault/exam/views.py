from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam, ExamAttempt, Answer
from questionbank.models import Question

from django.contrib.auth.decorators import login_required


@login_required
def exam_list(request):

    exams = Exam.objects.all()

    return render(request, "exam_list.html", {
        "exams": exams
    })

# Start Exam
def start_exam(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    questions = Question.objects.filter(bank=exam.question_bank)[:exam.total_questions]

    attempt = ExamAttempt.objects.create(
        student=request.user,
        exam=exam,
        total_questions=len(questions)
    )

    return render(request, "exam_page.html", {
        "exam": exam,
        "questions": questions,
        "attempt": attempt
    })


# Submit Exam
def submit_exam(request, attempt_id):

    attempt = get_object_or_404(ExamAttempt, id=attempt_id)

    questions = Question.objects.filter(bank=attempt.exam.question_bank)[:attempt.total_questions]

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


# Exam Result
def exam_result(request, attempt_id):

    attempt = get_object_or_404(ExamAttempt, id=attempt_id)

    answers = Answer.objects.filter(attempt=attempt)

    return render(request, "exam_result.html", {
        "attempt": attempt,
        "answers": answers
    })
# Teacher Exam Dashboard
def teacher_exam_list(request):

    exams = Exam.objects.all()

    return render(request, "teacher_exam_list.html", {
        "exams": exams
    })