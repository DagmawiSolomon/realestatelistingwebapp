from django.db import models
from accounts.models import Agent

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Agent, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
