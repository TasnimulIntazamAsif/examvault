import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, QuestionBank


def upload_csv(request):
    if request.method == 'POST':

        file = request.FILES.get('file')
        bank_id = request.POST.get('bank')

        if not file:
            messages.error(request, "File not selected")
            return redirect('upload_csv')

        try:
            df = pd.read_csv(file)
            bank = QuestionBank.objects.get(id=bank_id)

            for _, row in df.iterrows():
                Question.objects.create(
                    bank=bank,
                    question_text=row['question'],
                    option_a=row['option_a'],
                    option_b=row['option_b'],
                    option_c=row['option_c'],
                    option_d=row['option_d'],
                    correct_option=row['correct_option'],
                    explanation=row.get('explanation', "")
                )

            messages.success(request, "CSV Uploaded Successfully!")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

        return redirect('upload_csv')

    banks = QuestionBank.objects.all()

    return render(request, 'questionbank/upload_csv.html', {
        'banks': banks
    })




def question_bank_list(request):
    banks = QuestionBank.objects.all()

    return render(request, 'questionbank/bank_list.html', {
        'banks': banks
    })


def view_questions(request, bank_id):
    questions = Question.objects.filter(bank_id=bank_id)

    return render(request, 'questionbank/view_questions.html', {
        'questions': questions
    })