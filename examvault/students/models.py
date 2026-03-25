from django.db import models
from django.conf import settings


class StudentProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    institution = models.CharField(max_length=200)

    # ✅ NEW FIELDS
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    class_name = models.CharField(max_length=50, blank=True)
    id_card = models.FileField(upload_to='student_ids/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name