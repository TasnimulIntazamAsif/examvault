from django.shortcuts import render,redirect
from questionbank.models import QuestionBank,Question

def add_question(request):

    banks = QuestionBank.objects.all()

    if request.method=="POST":

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

    return render(request,"add_question.html",{"banks":banks})