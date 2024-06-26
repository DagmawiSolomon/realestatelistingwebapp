from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("listing/",views.ListingsListView.as_view(), name="listing"),
    path("listing/<int:pk>/",views.ListingDetailView.as_view(), name="listing-detail"),
    path("agent/", views.AgentsListView.as_view(), name="agent",),
    path("agent/<int:pk>/", views.AgentsDetailView.as_view(), name="agent-detail"),
]