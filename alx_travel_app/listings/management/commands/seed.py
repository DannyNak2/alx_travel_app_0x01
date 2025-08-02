from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                'title': 'Beach House',
                'description': 'A beautiful house near the beach.',
                'location': 'Malibu',
                'price_per_night': 250.00,
                'available': True
            },
            {
                'title': 'Mountain Cabin',
                'description': 'A cozy cabin in the mountains.',
                'location': 'Aspen',
                'price_per_night': 180.00,
                'available': True
            },
            {
                'title': 'City Apartment',
                'description': 'Modern apartment in the city center.',
                'location': 'New York',
                'price_per_night': 300.00,
                'available': False
            },
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings."))
