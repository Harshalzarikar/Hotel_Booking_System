from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
    ]
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default='single')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    location = models.CharField(max_length=100, default='Main Building')
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['room_number']
    
    def __str__(self):
        return f"Room {self.room_number} - {self.get_room_type_display()}"
    
    def is_available_for_dates(self, check_in_date, check_out_date):
        """Check if room is available for given date range"""
        bookings = self.bookings.filter(
            models.Q(check_in_date__lt=check_out_date) & 
            models.Q(check_out_date__gt=check_in_date)
        ).exclude(status='cancelled')
        return not bookings.exists()


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Booking for {self.guest_name} - Room {self.room.room_number}"
    
    def save(self, *args, **kwargs):
        # Calculate total price based on number of nights
        if self.check_in_date and self.check_out_date and self.room_id:
            nights = (self.check_out_date - self.check_in_date).days
            self.total_price = nights * self.room.price_per_night
        super().save(*args, **kwargs)
    
    def clean(self):
        """Validation for booking dates"""
        from django.core.exceptions import ValidationError
        
        if self.check_in_date and self.check_out_date:
            if self.check_in_date >= self.check_out_date:
                raise ValidationError('Check-out date must be after check-in date.')
            
            if self.check_in_date < date.today():
                raise ValidationError('Check-in date cannot be in the past.')
