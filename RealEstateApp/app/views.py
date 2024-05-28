from typing import Any
from django.shortcuts import render
from .models import Listing, Agent
from django.views.generic import ListView,DetailView
from django.core.serializers.json import DjangoJSONEncoder
import json



class Home(ListView):
    model = Listing
    template_name = "app/home.html"


class ListingsView(ListView):
    paginate_by = 9
    model = Listing
    template_name = "app/listing.html"


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        listings = []
        for listing in Listing.objects.all():
            property = listing.property
            property_values =  {
                "id": listing.id,
                "title": property.title,
                "address": property.address,
                "bedrooms": property.bedrooms,
                "bathrooms": property.bathrooms,
                "sqm":property.square_footage,
                "price":property.price,
                "property_type":property.property_type,
                    'location': {
                'lat': property.location.y, 
                'lng': property.location.x,
            }
            }
            listings.append(property_values)
        context["qs_json"] = json.dumps(listings, cls=DjangoJSONEncoder)
        return context

class ListingDetailView(DetailView):
    model = Listing
    template_name = "app/listing-detail.html"


class Agents(ListView):
    paginate_by = 9
    model = Agent
    template_name = "app/agent.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        agents = list(Agent.objects.values('id','first_name','last_name','profile'))
        context["qs_json"] = json.dumps(agents, cls=DjangoJSONEncoder)
        return context
    
class AgentsDetailView(DetailView):
    model = Agent
    template_name = "app/agent-detail.html"