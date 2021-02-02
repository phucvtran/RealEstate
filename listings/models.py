from django.db import models
from datetime import datetime

from django.db.models.fields import CharField, NullBooleanField
from realtors.models import Realtor

# Create your models here.
# class Listing(models.Model):
#     realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
#     title = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=20)
#     description = models.TextField(blank=True)
#     price = models.IntegerField()
#     bedrooms = models.IntegerField()
#     bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
#     garage = models.IntegerField(default=0)
#     sqft = models.IntegerField()
#     lot_size = models.DecimalField(max_digits=5, decimal_places=1)
#     photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
#     photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
#     photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
#     photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
#     photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
#     photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
#     is_published = models.BooleanField(default=True)
#     list_date = models.DateTimeField(default=datetime.now, blank=True)
    
#     def __str__(self):
#         return self.title

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    listing_id = models.IntegerField()
    is_new_construction = models.BooleanField(blank=True)
    last_update = models.DateTimeField()
    rdc_web_url = models.URLField(max_length=200)
    address = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    neighborhood_name = models.CharField(max_length=200)
    property_status = models.CharField(max_length=100)
    price_raw = models.IntegerField()
    sqft_raw = models.IntegerField()
    list_date = models.DateTimeField(blank=True)
    office_name = models.CharField(max_length=200)
    is_showcase = models.BooleanField(default=False)
    price = models.CharField(max_length=20)
    beds = models.IntegerField()
    baths = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.CharField(max_length=50)
    lot_size = models.CharField(max_length=200)
    photo = models.URLField(max_length=200)
    short_price = CharField(max_length=50)
    is_new_listing = models.BooleanField()
    page_no = models.IntegerField()
    rank = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank = True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)

    
    def __str__(self):
        return self.address