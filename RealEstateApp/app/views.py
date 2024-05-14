from typing import Any
from django.shortcuts import render
from .models import Listing, Agent
from django.views.generic import ListView
from django.core.serializers.json import DjangoJSONEncoder
import json
import datetime
class Home(ListView):
    model = Listing
    template_name = "app/home.html"


class Listing(ListView):
    model = Listing
    template_name = "app/listing.html"

class Agents(ListView):
    model = Agent
    template_name = "app/agent.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        agents = list(Agent.objects.values('id','first_name','last_name','profile'))
        context["qs_json"] = json.dumps(agents, cls=DjangoJSONEncoder)
        return context