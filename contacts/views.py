from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from listings.models import Listing
from listings import  views
from btre import  settings


# Create your views here.
def contact(request):
    partial_url = request.POST['partial_url']
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        prop_status = request.POST['prop_status']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+partial_url+listing_id)

        # save listing to database here, run through the list
        contact = Contact(listing=listing, listing_id=listing_id,prop_status=prop_status, name=name,
        email=email, phone=phone, message=message,user_id=user_id)
        
        contact.save()
        has_listing = Listing.objects.all().filter(listing_id=listing_id, is_search_listing = False)
        if not has_listing:
            Save_Listing(request, listing_id)

        send_mail(
            'Property Listing Inquiry', # subject
            'There has been an inquiry for ' + listing+ '. Sign into the admin panel for more info', # body message
            'tran@pullova.com',
            ['tran@pullova.com', 'vtphuchn@yahoo.com', email],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to your soon.')

        return redirect('/listings/'+partial_url+listing_id)

def Save_Listing(request,listing_id):
    get_listing = Listing.objects.all().filter(listing_id = listing_id)
    # get the selected listing in listings list
    if request.method == 'POST':
        if get_listing:
            get_listing.update(is_search_listing=False)
        elif request.POST['prop_status'] == 'for_sale':
            for listing in settings.for_sale_data['listings']:
                if listing['listing_id'] == request.POST['listing_id']:
                    prop_list = listing
                    save_sale_listing(prop_list,False)
        elif  request.POST['prop_status'] == 'for_rent':
            for listing in settings.for_rent_data['listings']:
                if listing['listing_id'] == request.POST['listing_id']:
                    prop_list = listing
                    save_rent_listing(prop_list,False)
        
        
            
    

def save_sale_listing(prop_list, is_search_listing):
    is_search_listing = is_search_listing
    listing_id = prop_list['listing_id']
    prop_type = prop_list['prop_type']
    prop_status = prop_list['prop_status']
    last_update = prop_list['last_update']
    title = prop_list['address_new']['line']
    address = prop_list['address']
    city = prop_list['address_new']['city']
    postal_code = prop_list['address_new']['postal_code']
    state_code = prop_list['address_new']['state_code']
    state = prop_list['address_new']['state']
    price = prop_list['price']
    lat = prop_list['lat']
    lon = prop_list['lon']
    beds = prop_list['beds']
    baths = prop_list['baths']
    sqft = prop_list['sqft']
    list_date = prop_list['list_date']
    office_name = prop_list['office_name']
    rdc_web_url = prop_list['rdc_web_url']
    lot_size = ""
    neighborhood = ""
    photo =""
    try:
        neighborhood = prop_list['address_new']['neighborhoods'][0]['name'] 
    except KeyError:
        neighborhood = "N/A"      
    
    try:
        photo = prop_list['photo']
    except KeyError:
        photo = ""

    try:
        lot_size = prop_list['lot_size']  
    except KeyError:
        lot_size = "N/A"

    listing = Listing(
        is_search_listing = is_search_listing,
        listing_id = listing_id,
        prop_type = prop_type,
        prop_status = prop_status,
        last_update = last_update,
        list_date = list_date,
        office_name = office_name,
        title = title,
        address = address,
        city = city,
        postal_code = postal_code,
        state_code = state_code,
        state = state,
        neighborhood = neighborhood,
        price = price,
        lat = lat,
        lon = lon,
        beds = beds,
        baths = baths,
        sqft = sqft,
        lot_size = lot_size,
        rdc_web_url = rdc_web_url,
        photo = photo)

    listing.save()

def save_rent_listing(prop_list, is_search_listing):
    is_search_listing = is_search_listing
    listing_id = prop_list['listing_id']
    prop_type = prop_list['prop_type']
    prop_status = prop_list['prop_status']
    last_update = prop_list['last_update']
    title = prop_list['address_new']['line']
    address = prop_list['address']
    city = prop_list['address_new']['city']
    postal_code = prop_list['address_new']['postal_code']
    state_code = prop_list['address_new']['state_code']
    state = prop_list['address_new']['state']
    price = prop_list['price']
    lat = prop_list['lat']
    lon = prop_list['lon']
    beds = prop_list['beds']
    baths = prop_list['baths']
    sqft = prop_list['sqft']
    neighborhood = ""
    photo=""
    try:
        neighborhood = prop_list['name']
    except KeyError:
        neighborhood = "N/A"

    try:
        photo = prop_list['photo']
    except KeyError:
        photo = ""


    listing = Listing(
        is_search_listing = is_search_listing,
        listing_id = listing_id,
        prop_type = prop_type,
        prop_status = prop_status,
        last_update = last_update,
        list_date = '',
        office_name = "N/A",
        title = title,
        address = address,
        city = city,
        postal_code = postal_code,
        state_code = state_code,
        state = state,
        neighborhood = neighborhood,
        price = price,
        lat = lat,
        lon = lon,
        beds = beds,
        baths = baths,
        sqft = sqft,
        lot_size = "N/A",
        rdc_web_url = "N/A",
        photo = photo)

    listing.save()
