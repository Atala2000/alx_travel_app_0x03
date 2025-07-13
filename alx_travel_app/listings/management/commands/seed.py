import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create a user to assign as host if none exists
        if not User.objects.filter(username='hostuser').exists():
            user = User.objects.create_user(username='hostuser', password='password123')
        else:
            user = User.objects.get(username='hostuser')

        # Sample listings data
        sample_listings = [
            {'title': 'Cozy Cottage', 'description': 'A nice cozy cottage.', 'location': 'Countryside', 'price_per_night': 75.00},
            {'title': 'City Apartment', 'description': 'Modern apartment in city center.', 'location': 'City', 'price_per_night': 120.00},
            {'title': 'Beach House', 'description': 'House with ocean view.', 'location': 'Beach', 'price_per_night': 200.00},
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'location': data['location'],
                    'price_per_night': data['price_per_night'],
                    'host': user,
                }
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully with sample listings.'))
