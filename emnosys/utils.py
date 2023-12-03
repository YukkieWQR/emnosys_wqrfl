from django.conf import settings
from emnosys.models import Contact
from django.core.mail import send_mass_mail, EmailMessage
def SendEmail():
    message1 = EmailMessage(
        "Subject here",
        "Here is the message",
        "emnosys.wqrfl@gmail.com",
        ["pawwne27@gmail.com"],
    )

    message_tuple = ((message1.subject, message1.body, message1.from_email, message1.to),)

    send_mass_mail(message_tuple, fail_silently=False)