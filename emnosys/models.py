from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    username = models.CharField(max_length=255, null=False)
    message = models.TextField(null=False)
    email = models.EmailField(max_length=99, null=False)
