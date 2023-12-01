from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    username = models.CharField(max_length=255, null=False)
    message = models.TextField(null=False)
    email = models.EmailField(max_length=99, null=False)
    contactowner = models.ForeignKey(User, on_delete=models.CASCADE)