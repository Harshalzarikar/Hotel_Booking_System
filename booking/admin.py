from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'room_type', 'price_per_night', 'capacity', 'location', 'is_available']
    list_filter = ['room_type', 'is_available', 'location']
    search_fields = ['room_number', 'description']
    list_editable = ['is_available']
    ordering = ['room_number']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['guest_name', 'room', 'check_in_date', 'check_out_date', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'check_in_date', 'created_at']
    search_fields = ['guest_name', 'guest_email', 'guest_phone', 'room__room_number']
    date_hierarchy = 'check_in_date'
    readonly_fields = ['total_price', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Guest Information', {
            'fields': ('guest_name', 'guest_email', 'guest_phone')
        }),
        ('Booking Details', {
            'fields': ('room', 'check_in_date', 'check_out_date', 'number_of_guests', 'total_price')
        }),
        ('Additional Information', {
            'fields': ('status', 'special_requests', 'created_at', 'updated_at')
        }),
    )
