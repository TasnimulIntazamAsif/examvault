from django.db import models
from django.conf import settings


class TeacherProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)

    # ✅ NEW FIELDS
    image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    experience = models.IntegerField(default=0)
    id_card = models.FileField(upload_to='teacher_ids/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name