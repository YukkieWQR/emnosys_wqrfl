from emnosys.models import Contact
from django.core.mail import send_mail

def SendEmailView():
    subject = "boooooooooooooooo"
    message = "emnosy send you this messhige"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["pawwne27@gmail.com"]


    send_mail(subject, message, from_email, recipient_list)