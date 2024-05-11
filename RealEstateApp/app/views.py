from typing import Any
from django.shortcuts import render
from .models import Listing, Agent
from django.views.generic import ListView


class Home(ListView):
    model = Listing
    template_name = "app/home.html"


class Listing(ListView):
    model = Listing
    template_name = "app/listing.html"

class Agents(ListView):
    model = Agent
    template_name = "app/agent.html"