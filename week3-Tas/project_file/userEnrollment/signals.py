from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Enrollment

# Signal to send an email after enrollment is saved
@receiver(post_save, sender=Enrollment)
def send_enrollment_email(sender, instance, created, **kwargs):
    if created:  # Only send email when a new enrollment is created
        user = instance.user
        course = instance.course
        
        # Send the email
        send_mail(
            subject=f"Enrolled in {course.title}",
            message=f"Hello {user.username},\n\nYou have been successfully enrolled in the course: {course.title}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
