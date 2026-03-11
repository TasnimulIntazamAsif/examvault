from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exam, ExamAttempt, Answer

admin.site.register(Exam)
admin.site.register(ExamAttempt)
admin.site.register(Answer)