from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import auth
from django.shortcuts import get_object_or_404, render
import requests, json

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import state_choices, price_choices, bedroom_choices

from .models import Listing

# Create your views here.
def index(request):
    """
    docstring
    """
    # listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    listings = Listing
    listings.objects.create(address = 'hello')
    print(listings.address)
    
    # call Realtor api to get listing,
    # default listing is set to SEATTLE, WASHINGTON
    # url = "https://realtor.p.rapidapi.com/properties/list-for-sale"

    # querystring = {"city":"Seattle","offset":"0","limit":"31","state_code":"WA","sort":"relevance"}

    # headers = {
    #     'x-rapidapi-key': "9967758667mshf478a6da53e4ff2p1a58cejsn50a1568fe9aa",
    #     'x-rapidapi-host': "realtor.p.rapidapi.com"
    #     }

    # response = requests.request("GET", url, headers=headers, params=querystring)

    # data = json.loads(response.text)

    with open('listings\outputfile.json') as f:
        data = json.load(f)

    # print (data['listings'][0])

    # for listing in data['listings'][0]:
    #     print()
        

    # paginator = Paginator(listings, 6)
    # page = request.GET.get('page')
    # paged_listings= paginator.get_page(page)

    # context = {
    #     'listings': paged_listings,
    # }

    return render(request, 'listings/listings.html')

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