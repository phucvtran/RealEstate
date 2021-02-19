from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from listings.models import Listing
from btre import settings


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
        has_listing = Listing.objects.all().filter(listing_id=listing_id)
        if not has_listing:
            Save_Listing(request)

        send_mail(
            'Property Listing Inquiry', # subject
            'There has been an inquiry for ' + listing+ '. Sign into the admin panel for more info', # body message
            'tran@pullova.com',
            ['tran@pullova.com', 'vtphuchn@yahoo.com', email],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to your soon.')

        return redirect('/listings/'+partial_url+listing_id)

def Save_Listing(request):
    prop_list = {}
    
    # get the selected listing in listings list
    if request.method == 'POST':
        if settings.search_data:
            for listing in settings.search_data['listings']:
                if listing['listing_id'] == request.POST['listing_id']:
                    prop_list = listing
        elif request.POST['prop_status'] == 'for_sale':
            for listing in settings.for_sale_data['listings']:
                if listing['listing_id'] == request.POST['listing_id']:
                    prop_list = listing
        elif  request.POST['prop_status'] == 'for_rent':
            for listing in settings.for_rent_data['listings']:
                if listing['listing_id'] == request.POST['listing_id']:
                    prop_list = listing
    try:
        listing_id = prop_list['listing_id']
        prop_type = prop_list['prop_type']
        prop_status = prop_list['prop_status']
        last_update = prop_list['last_update']
        list_date = prop_list['list_date']
        office_name = prop_list['office_name']
        title = prop_list['address']
        address = prop_list['address']
        city = prop_list['address_new']['city']
        postal_code = prop_list['address_new']['postal_code']
        state_code = prop_list['address_new']['state_code']
        state = prop_list['address_new']['state']
        neighborhood = prop_list['address_new']['neighborhoods'][0]['name']
        price_raw = prop_list['price_raw']
        price = prop_list['price']
        lat = prop_list['lat']
        lon = prop_list['lon']
        beds = prop_list['beds']
        baths = prop_list['baths']
        sqft = prop_list['sqft']
        sqft_raw = prop_list['sqft_raw']
        lot_size = prop_list['lot_size']
        rdc_web_url = prop_list['rdc_web_url']
        photo = prop_list['photo']
    except  KeyError:
        pass
    except  None:
        pass

    listing = Listing(
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
        price_raw = price_raw,
        price = price,
        lat = lat,
        lon = lon,
        beds = beds,
        baths = baths,
        sqft = sqft,
        sqft_raw = sqft_raw,
        lot_size = lot_size,
        rdc_web_url = rdc_web_url,
        photo = photo)

    listing.save()
