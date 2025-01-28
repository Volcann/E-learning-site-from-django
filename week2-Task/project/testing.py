from django.core.mail import send_mail
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
django.setup()

send_mail(
    subject='Test',
    message='This id s ',
    from_email="muhammad.mohsin@folium.ai",
    recipient_list=["mohsinmuhammad823@gmail.com"],
    fail_silently=False,
)
