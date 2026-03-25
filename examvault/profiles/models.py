from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# ========================
# STUDENT PROFILE
# ========================
class StudentProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    class_name = models.CharField(max_length=50, blank=True)
    school_name = models.CharField(max_length=200, blank=True)

    id_card = models.FileField(upload_to='student_ids/', null=True, blank=True)

    def __str__(self):
        return self.user.username


# ========================
# TEACHER PROFILE
# ========================
class TeacherProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    subject = models.CharField(max_length=100, blank=True)
    experience = models.IntegerField(default=0)

    id_card = models.FileField(upload_to='teacher_ids/', null=True, blank=True)

    def __str__(self):
        return self.user.username