from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return render(request, "registration/logout.html")