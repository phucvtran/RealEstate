from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import auth
from django.shortcuts import get_object_or_404, render

import requests, json

import re

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import state_choices, price_choices, bedroom_choices

from .models import Listing
from pages.views import readfile

# Create your views here.
def index(request):
    """
    docstring
    """


    data = readfile('forsalelisting.json')

    print(data)

    # print('type of data is :')
    # print(type(data))
    # print (data['listings'][0])

    # for listing in data['listings'][0]:
    #     print()
        
    # l =data['listings'][:]
    # print(l[:]['last_update'])

    paginator = Paginator(data['listings'], 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    
    context = {
        'listings': paged_listings,
        
    }
    
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    """
    single listing
    docstring
    """
    listing = get_object_or_404(Listing, pk = listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    """
    docstring
    """
    queryset_list = Listing.objects.order_by('-list_date')

    # Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)

    # bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms) # lte = less than or equal to


    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)

    
    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
        
    }
    return render(request, 'listings/search.html', context)