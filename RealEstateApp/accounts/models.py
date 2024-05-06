from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractUser):

    phonenumber = PhoneNumberField(blank=True, help_text='Phonenumber')
    def __str__(self):
        return self.username
    

class Agent(AbstractUser):
    user = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE)
    profile = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name="Firstname")
    last_name = models.CharField(max_length=255, verbose_name="Lastname")
    groups = models.ManyToManyField(Group, related_name='agent_set')  
    user_permissions = models.ManyToManyField(Permission, related_name='agent_set')

    class Meta:
        verbose_name = "Agent"
    def __str__(self) -> str:
        return f"Agent - {self.first_name} {self.last_name}"

