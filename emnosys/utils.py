from django.conf import settings
from emnosys.models import Contact
from django.core.mail import send_mail, EmailMessage
from .models import Contact
from django.shortcuts import render
from django.template.loader import render_to_string

def SendEmail(request):
    username = request.user.username
    all_contacts = Contact.objects.filter(contactowner__username=username)

    for cntct in all_contacts:
        personalized_message = cntct.message
        email = EmailMessage(
            'Someone used our application to send you this emergency message!',
            personalized_message,
            'emnosy.wqrfl@gmail.com',
            [cntct.email],
        )
        email.content_subtype = 'html'  # Set the content type to HTML
        email.send(fail_silently=False)
