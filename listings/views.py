from django.shortcuts import get_object_or_404, render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    """
    docstring
    """
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings= paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    """
    single listing
    docstring
    """
    listing = get_object_or_404(Listing, pk = listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    """
    docstring
    """
    return render(request, 'listings/search.html')