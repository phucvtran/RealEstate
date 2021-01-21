from django.urls import path

from . import views

# if we leave the path blank it refer to /listings
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]