from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator 


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

class AgentRating(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0.0)


    def calculate_rating(self):
        return self.rating/self.rating_count
    
    def save(self, *args, **kwargs):
        if not self.average_rating:
            self.average_rating = self.calculate_rating()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.agent.first_name} {self.agent.last_name} - {self.average_rating} rating"
    
    