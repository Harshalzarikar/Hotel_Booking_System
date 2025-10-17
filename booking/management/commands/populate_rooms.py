from django.core.management.base import BaseCommand
from booking.models import Room

class Command(BaseCommand):
    help = 'Populate the database with sample hotel rooms'

    def handle(self, *args, **kwargs):
        rooms_data = [
            {
                'room_number': '101',
                'room_type': 'single',
                'price_per_night': 99.99,
                'capacity': 1,
                'location': 'First Floor - East Wing',
                'description': 'Cozy single room with city view, perfect for solo travelers.',
                'is_available': True
            },
            {
                'room_number': '102',
                'room_type': 'single',
                'price_per_night': 99.99,
                'capacity': 1,
                'location': 'First Floor - East Wing',
                'description': 'Comfortable single room with modern amenities.',
                'is_available': True
            },
            {
                'room_number': '201',
                'room_type': 'double',
                'price_per_night': 149.99,
                'capacity': 2,
                'location': 'Second Floor - West Wing',
                'description': 'Spacious double room with queen-size bed and garden view.',
                'is_available': True
            },
            {
                'room_number': '202',
                'room_type': 'double',
                'price_per_night': 159.99,
                'capacity': 2,
                'location': 'Second Floor - West Wing',
                'description': 'Elegant double room with balcony and sunset view.',
                'is_available': True
            },
            {
                'room_number': '301',
                'room_type': 'suite',
                'price_per_night': 299.99,
                'capacity': 3,
                'location': 'Third Floor - Premium Wing',
                'description': 'Luxurious suite with separate living area, kitchenette, and panoramic city views.',
                'is_available': True
            },
            {
                'room_number': '302',
                'room_type': 'suite',
                'price_per_night': 329.99,
                'capacity': 4,
                'location': 'Third Floor - Premium Wing',
                'description': 'Executive suite with workspace, mini-bar, and premium amenities.',
                'is_available': True
            },
            {
                'room_number': '401',
                'room_type': 'deluxe',
                'price_per_night': 449.99,
                'capacity': 4,
                'location': 'Fourth Floor - Penthouse',
                'description': 'Premium deluxe room with jacuzzi, private terrace, and butler service.',
                'is_available': True
            },
            {
                'room_number': '402',
                'room_type': 'deluxe',
                'price_per_night': 499.99,
                'capacity': 5,
                'location': 'Fourth Floor - Penthouse',
                'description': 'Presidential suite with two bedrooms, full kitchen, and exclusive lounge access.',
                'is_available': True
            },
        ]
        
        for room_data in rooms_data:
            room, created = Room.objects.get_or_create(
                room_number=room_data['room_number'],
                defaults=room_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created room {room.room_number}'))
            else:
                self.stdout.write(self.style.WARNING(f'Room {room.room_number} already exists'))
        
        self.stdout.write(self.style.SUCCESS('Successfully populated hotel rooms')) 