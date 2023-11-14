from django.db import models
from django.core.validators import RegexValidator
class Contact(models.Model):
    name = models.CharField(max_length=255)

    message = models.TextField()

    nickname = models.CharField(
        max_length=30,
        validators=[RegexValidator(r'^@.+$', 'Nickname must start with "@"')],
    )
