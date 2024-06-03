from django.db import models
from accounts.models import Agent,CustomUser

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.title
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Agent, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author
    