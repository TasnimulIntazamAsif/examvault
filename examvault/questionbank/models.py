from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionBank(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):

    bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

    question_text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(max_length=1)

    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text