from .models import Listing, Booking
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'host', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'start_date', 'end_date', 'total_price', 'created_at']
