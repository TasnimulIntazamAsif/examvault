from django.shortcuts import render
from questionbank.models import QuestionBank


def question_banks(request):

    banks = QuestionBank.objects.all()

    return render(request, "question_banks.html", {"banks": banks})