from django.core.mail import send_mail
from django.conf import settings



def send_user_mail(mail: str) -> bool:
    subject = 'Welcome to My Site'
    message = 'Thank you for creating an account!'
    recipient_list = [mail]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
    return True
