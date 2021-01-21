from django.shortcuts import render

# Create your views here.
def index(request):
    """
    docstring
    """
    return render(request, 'listings/listings.html')

def listing(request):
    """
    docstring
    """
    return render(request, 'listings/listing.html')

def search(request):
    """
    docstring
    """
    return render(request, 'listings/search.html')