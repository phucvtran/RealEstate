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

for_sale_data = readfile('forsalelisting.json')
for_rent_data = readfile('forrentlisting.json')
# Create your views here.
def index(request):
    """
    docstring
    """

    # for sale 
    paginator = Paginator(for_sale_data['listings'], 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    # for rent
    paginator_rent = Paginator(for_rent_data['listings'], 6)
    page_rent = request.GET.get('page')
    paged_listings_rent= paginator_rent.get_page(page_rent)

    
    context = {
        'sale_listings': paged_listings,  
        'rent_listings': paged_listings_rent   
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

def sale(request):

    paginator = Paginator(for_sale_data['listings'], 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    
    context = {
        'listings': paged_listings,
        
    }
    
    return render(request, 'listings/for_sale_listings.html',context)

def rent(request):

    paginator = Paginator(for_rent_data['listings'], 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    
    context = {
        'listings': paged_listings,
        
    }
    
    return render(request, 'listings/for_rent_listings.html',context)

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