from django.db import models
from django.contrib.auth import get_user_model
from questionbank.models import QuestionBank, Question

User = get_user_model()


class Exam(models.Model):

    title = models.CharField(max_length=200)
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    total_questions = models.IntegerField()

    def __str__(self):
        return self.title


class ExamAttempt(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    score = models.IntegerField(default=0)

    total_questions = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    unanswered = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exam}"


class Answer(models.Model):

    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    selected_option = models.CharField(max_length=1, blank=True)

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question}"