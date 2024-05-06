from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import (Agent)
# Register your models here.

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["phonenumber","email","username",]
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Agent)
