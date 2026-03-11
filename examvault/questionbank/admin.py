from django.contrib import admin
from .models import Subject, QuestionBank, Question

admin.site.register(Subject)
admin.site.register(QuestionBank)
admin.site.register(Question)