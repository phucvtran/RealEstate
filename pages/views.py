from realtors.models import Realtor
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
import json
from listings.choices import state_choices, price_choices, bedroom_choices

def index(request):
    # listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    # context = {
    #     'listings': listings,
    #     'state_choices': state_choices,
    #     'bedroom_choices': bedroom_choices, 
    #     'price_choices': price_choices
    # }

    data = readfile('forsalelisting.json')

    context = {
        'listings' : data['listings'][:3],
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices, 
        'price_choices': price_choices
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

def readfile(filename):
    with open(filename) as f:
        data = json.load(f)
        f.close()
        return data
