from typing import Any
from django.shortcuts import render
from .models import Listing
from django.views.generic import ListView


class Home(ListView):
    model = Listing
    template_name = "app/home.html"
