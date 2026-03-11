from django.db import models


class Subject(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class QuestionBank(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    year = models.IntegerField()

    is_premium = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class Question(models.Model):

    bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

    question_text = models.TextField()

    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)

    correct_option = models.CharField(max_length=1)

    explanation = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text