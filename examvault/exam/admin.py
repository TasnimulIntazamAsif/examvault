from django.contrib import admin
from .models import Exam, ExamAttempt, Answer


# =========================
# EXAM ADMIN (IMPORTANT 🔥)
# =========================
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = ('title',)

    # 🔥 THIS ENABLES MULTI SELECT UI
    filter_horizontal = ('questions',)

    search_fields = ('title',)


# =========================
# EXAM ATTEMPT ADMIN
# =========================
@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'exam',
        'score',
        'correct',
        'wrong',
        'unanswered',
        'created_at'
    )

    list_filter = ('exam', 'created_at')


# =========================
# ANSWER ADMIN
# =========================
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = ('attempt', 'question', 'selected_option', 'is_correct')

    list_filter = ('is_correct',)