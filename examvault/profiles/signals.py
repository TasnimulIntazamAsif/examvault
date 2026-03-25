from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import StudentProfile, TeacherProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        if instance.role == 'student':
            StudentProfile.objects.create(user=instance)

        elif instance.role == 'teacher':
            TeacherProfile.objects.create(user=instance)