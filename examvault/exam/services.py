from .models import ExamAttempt, Answer


def create_attempt(user, exam):

    attempt = ExamAttempt.objects.filter(
        student=user,
        exam=exam
    ).first()

    if attempt:
        return attempt

    questions = exam.questions.all()

    attempt = ExamAttempt.objects.create(
        student=user,
        exam=exam,
        total_questions=questions.count()
    )

    attempt.questions.set(questions)

    return attempt


def evaluate_exam(attempt, request):

    correct = 0
    wrong = 0
    unanswered = 0

    for q in attempt.questions.all():

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
            selected_option=selected or "",
            is_correct=is_correct
        )

    attempt.correct = correct
    attempt.wrong = wrong
    attempt.unanswered = unanswered
    attempt.score = correct
    attempt.save()

    return attempt