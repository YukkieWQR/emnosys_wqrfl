# Generated by Django 3.2.23 on 2023-12-17 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emnosys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='auth_token',
            new_name='token',
        ),
    ]