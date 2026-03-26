from django.contrib import admin
from .models import Subject, QuestionBank, Question


# =========================
# QUESTION INLINE (🔥 inside bank)
# =========================
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


# =========================
# SUBJECT ADMIN
# =========================
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

    search_fields = ('name',)


# =========================
# QUESTION BANK ADMIN
# =========================
@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'subject')

    list_filter = ('subject',)

    search_fields = ('title',)

    # 🔥 show questions inside bank
    inlines = [QuestionInline]


# =========================
# QUESTION ADMIN
# =========================
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = ('id', 'question_text', 'bank', 'correct_option')

    list_filter = ('bank',)

    search_fields = ('question_text',)