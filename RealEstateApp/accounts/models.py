from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractUser):
    phonenumber = PhoneNumberField(blank=True, help_text='Phonenumber')
    def __str__(self):
        return self.username

