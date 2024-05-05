from django.urls import path
from django.contrib.auth import views
from . import views as customview

urlpatterns = [
   path("signup/", customview.SignUpView.as_view(), name="signup"),
   path("login/", views.LoginView.as_view(), name="login"),
   path("logout/", views.LogoutView.as_view(), name="logout"),
]