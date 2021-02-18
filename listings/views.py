from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import auth
from django.shortcuts import get_object_or_404, render,redirect

import requests, json

from btre import settings

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import state_choices, price_choices, bedroom_choices, search_choices, price_choices_rent

from .models import Listing
from pages.views import readfile

for_sale_data = readfile('forsalelisting.json')
for_rent_data = readfile('forrentlisting.json')
search_data = {}
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
        'rent_listings': paged_listings_rent,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_choices': search_choices,
        'price_choices_rent': price_choices_rent
    }
    
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    """
    single listing
    docstring
    """

    return_data = []

    if (search_data):

        for listing in search_data['listings']:
            if listing['listing_id'] == listing_id:
                return_data = listing
    else:

        if 's_listing' in request.path_info:
            for listing in for_sale_data['listings']:
                if listing['listing_id'] == listing_id:
                    return_data = listing
        elif 'r_listing' in request.path_info:
            for listing in for_rent_data['listings']:
                if listing['listing_id'] == listing_id:
                    return_data = listing

    context = {
        'listing': return_data,
    }

    return render(request, 'listings/listing.html', context)

def sale(request):

    paginator = Paginator(for_sale_data['listings'], 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    
    context = {
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_choices': search_choices,
        'price_choices_rent': price_choices_rent
        
    }
    
    return render(request, 'listings/for_sale_listings.html',context)

def rent(request):

    paginator = Paginator(for_rent_data['listings'], 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    
    context = {
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_choices': search_choices,
        'price_choices_rent': price_choices_rent
        
        
    }
    
    return render(request, 'listings/for_rent_listings.html',context)

def search(request):
    """
    docstring
    """
    url = "https://realtor.p.rapidapi.com/properties/"
    querystring = {
        "offset":"0",
        "limit": settings.REALTOR_API_SALE_LIMIT,
        "city" : settings.REALTOR_API_DEFAULT_CITY,
        "sort":"relevance",
    }

    searchmethod = ""

    headers = {
        'x-rapidapi-key': settings.REALTOR_API_KEY,
        'x-rapidapi-host': settings.REALTOR_API_HOST
        }

    # Keyword
    if 'search' in request.GET:
        search = request.GET['search']           
        if search:
            url=url+search
            searchmethod = search
        if 'sale' in search:
            if 'price' in request.GET:
                price = request.GET['price']
                if price:
                    querystring['price_max'] = price
        elif 'rent' in search:
            querystring["limit"] = settings.REALTOR_API_RENT_LIMIT
            if 'price-rent' in request.GET:
                price_rent = request.GET['price-rent']
                if '2000' in price_rent:
                    querystring['price_min'] = price_rent
                else:
                    querystring['price_max'] = str(int(price_rent) + 200)
                    querystring['price_min'] = price_rent
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querystring['city'] = city
            

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querystring['state_code'] = state

    # bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querystring['beds_min'] = bedrooms


    response = requests.request("GET", url, headers=headers, params=querystring)
    # data = readfile('searchlisting.json')
    data = json.loads(response.text)
    
    global search_data
    search_data = data



    context = {
        'listings': search_data['listings'],
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_choices': search_choices,
        'price_choices_rent': price_choices_rent,
        'values': querystring,
        'searchmethod': searchmethod
        
    }
    return render(request, 'listings/search.html', context)