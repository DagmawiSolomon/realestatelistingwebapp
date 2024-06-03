from django.db import models
from accounts.models import Agent,CustomUser

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title
        
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Agent, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)