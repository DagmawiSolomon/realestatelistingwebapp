from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("listing/",views.Listing.as_view(), name="listing"),
    path("agent/", views.Agents.as_view(), name="agent",)
]