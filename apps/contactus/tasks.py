import time
from celery import shared_task
from django.core.mail import send_mail



@shared_task()
def send_contact_email_task(email, full_name, subject, message):
    time.sleep(5)
    send_mail(
        from_email=email,
        recipient_list = ["aayobam@gmail.com",],
        subject=subject,
        message=f"{full_name}\n{message}",
        fail_silently=False
    )
