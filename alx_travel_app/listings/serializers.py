# listings/serializers.py

"""
Serializers for the listings app.

This module defines how Listing and Booking model instances are converted
to and from JSON representations for use in the API.
"""

from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.

    Converts Listing instances to JSON format and vice versa.
    All model fields are included in the serialization.
    """
    class Meta:
        model = Listing
        fields = '__all__'  # Include all fields from the Listing model


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.

    Converts Booking instances to JSON format and vice versa.
    All model fields are included in the serialization.
    """
    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields from the Booking model
