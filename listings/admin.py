from django.contrib import admin

from .models import Listing
from btre import settings
import requests, json


def for_sale_API(modeladmin, request, queryset):
    # call Realtor api to get listing,
    # default listing is set to SEATTLE, WASHINGTON
    url = settings.REALTOR_API_FORSALE_URL

    querystring = {"city":"Seattle","offset":"0","limit": "30","state_code":"WA","sort":"relevance"}

    headers = {
        'x-rapidapi-key': settings.REALTOR_API_KEY,
        'x-rapidapi-host': settings.REALTOR_API_HOST
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    with open('forsalelisting.json', 'wb') as outf:
        outf.write(response.content)
        outf.close()

def for_rent_API(modeladmin, request, queryset):
    # call Realtor api to get listing,
    # default listing is set to SEATTLE, WASHINGTON
    url = settings.REALTOR_API_FORRENT_URL

    querystring = {"city":"Seattle","offset":"0","limit": "20","state_code":"WA","sort":"relevance"}

    headers = {
        'x-rapidapi-key': settings.REALTOR_API_KEY,
        'x-rapidapi-host': settings.REALTOR_API_HOST
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    with open('forrentlisting.json', 'wb') as outf:
        outf.write(response.content)
        outf.close()

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'address')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('address', 'description', 'address', 'city',
    'state', 'zipcode', 'price')
    list_per_page = 25

    # action in listing admin page
    actions = [for_sale_API, for_rent_API] 

# Register your models here.
admin.site.register(Listing, ListingAdmin)
