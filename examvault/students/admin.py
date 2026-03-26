from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'institution', 'class_name')
    search_fields = ('full_name', 'phone')