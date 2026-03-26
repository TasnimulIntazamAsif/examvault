from django.contrib import admin
from .models import Exam, ExamAttempt, Answer


# =========================
# ANSWER INLINE (🔥 inside attempt)
# =========================
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


# =========================
# EXAM ADMIN
# =========================
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'total_questions')

    search_fields = ('title',)

    # 🔥 multi select UI
    filter_horizontal = ('questions',)


# =========================
# EXAM ATTEMPT ADMIN
# =========================
@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'exam',
        'score',
        'correct',
        'wrong',
        'unanswered',
        'created_at'
    )

    list_filter = ('exam', 'created_at')

    search_fields = ('student__username', 'exam__title')

    # 🔥 show answers inside attempt
    inlines = [AnswerInline]


# =========================
# ANSWER ADMIN
# =========================
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = ('attempt', 'question', 'selected_option', 'is_correct')

    list_filter = ('is_correct',)

    search_fields = ('question__question_text',)