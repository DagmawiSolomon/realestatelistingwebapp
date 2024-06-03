from django.contrib import admin
from accounts.models import CustomUser
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    exclude = ['author']   
    
    def save_model(self, request, obj, form, change):
        try:
            user = request.user            
            agent = Agent.objects.get(user=user)
            obj.author = agent
            obj.save()
            
        except Agent.DoesNotExist:
            # Handle the case where the Agent does not exist
            print("No agent")

admin.site.register(Post,PostAdmin)
admin.site.register(Category)

"""
Cannot resolve keyword 'CustomUser' into field.
Choices are: agentrating, date_joined, email, first_name, 
groups, id, is_active, is_staff, is_superuser, last_login, 
last_name, listing, password, post, profile, user, user_id, u
ser_permissions, username
"""