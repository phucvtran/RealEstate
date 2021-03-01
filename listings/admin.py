from django.contrib import admin

from .models import Listing
from btre import settings
import requests, json


def for_sale_API(modeladmin, request, queryset):
    # call Realtor api to get listing,
    # default listing is set to SEATTLE, WASHINGTON
    url = settings.REALTOR_API_FORSALE_URL

    querystring = {
        "city":settings.REALTOR_API_DEFAULT_CITY,
        "offset":"0",
        "limit": settings.REALTOR_API_SALE_LIMIT,
        "state_code":settings.REALTOR_API_DEFAULT_STATE,
        "sort":"relevance"}

    headers = {
        'x-rapidapi-key': settings.REALTOR_API_KEY,
        'x-rapidapi-host': settings.REALTOR_API_HOST
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # data = json.loads(response.text)

    with open('forsalelisting.json', 'wb') as outf:
        outf.write(response.content)
        outf.close()
    global for_rent_data
    for_rent_data = settings.readfile('forrentlisting.json')

def for_rent_API(modeladmin, request, queryset):
    # call Realtor api to get listing,
    # default listing is set to SEATTLE, WASHINGTON
    url = settings.REALTOR_API_FORRENT_URL

    querystring = {
        "city":settings.REALTOR_API_DEFAULT_CITY,
        "offset":"0",
        "limit": settings.REALTOR_API_RENT_LIMIT,
        "state_code":settings.REALTOR_API_DEFAULT_STATE,
        "sort":"relevance"}

    headers = {
        'x-rapidapi-key': settings.REALTOR_API_KEY,
        'x-rapidapi-host': settings.REALTOR_API_HOST
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # data = json.loads(response.text)

    with open('forrentlisting.json', 'wb') as outf:
        outf.write(response.content)
        outf.close()
    global for_rent_data
    for_rent_data = settings.readfile('forrentlisting.json')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'address','is_search_listing', 'price', 'list_date')
    list_display_links = ('listing_id', 'address')
    # list_filter = ('realtor',)
    # list_editable = ('is_published',)
    search_fields = ('address', 'description', 'address', 'city',
    'state', 'zipcode', 'price')
    list_per_page = 25

    # action in listing admin page
    actions = [for_sale_API, for_rent_API] 

# Register your models here.
admin.site.register(Listing, ListingAdmin)
