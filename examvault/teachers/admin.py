from django.contrib import admin
from .models import TeacherProfile

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'subject', 'experience')
    search_fields = ('full_name', 'phone', 'subject')