from realtors.models import Realtor
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
import json
from listings.choices import state_choices, price_choices, bedroom_choices, search_choices, price_choices_rent

from btre import settings

def index(request):
    # listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    # context = {
    #     'listings': listings,
    #     'state_choices': state_choices,
    #     'bedroom_choices': bedroom_choices, 
    #     'price_choices': price_choices
    # }
    # settings.init()

    context = {
        'sale_listings' : settings.for_sale_data['listings'][:3],
        'rent_listings': settings.for_rent_data['listings'][:3],
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'price_choices': price_choices,
        'price_choices_rent': price_choices_rent,
        'search_choices': search_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # get all Realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html', context)


