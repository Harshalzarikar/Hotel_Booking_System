from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Room, Booking
from .forms import BookingForm, RoomSearchForm
from datetime import date

def room_list(request):
    """List all available hotel rooms with optional search filters"""
    rooms = Room.objects.filter(is_available=True)
    form = RoomSearchForm(request.GET or None)
    
    if form.is_valid():
        room_type = form.cleaned_data.get('room_type')
        location = form.cleaned_data.get('location')
        max_price = form.cleaned_data.get('max_price')
        
        if room_type:
            rooms = rooms.filter(room_type=room_type)
        if location:
            rooms = rooms.filter(location__icontains=location)
        if max_price:
            rooms = rooms.filter(price_per_night__lte=max_price)
    
    context = {
        'rooms': rooms,
        'form': form,
    }
    return render(request, 'booking/room_list.html', context)

def room_detail(request, room_id):
    """Display details of a single room"""
    room = get_object_or_404(Room, id=room_id)
    
    # Get upcoming bookings for this room
    upcoming_bookings = room.bookings.filter(
        status='confirmed',
        check_out_date__gte=date.today()
    ).order_by('check_in_date')[:5]
    
    context = {
        'room': room,
        'upcoming_bookings': upcoming_bookings,
    }
    return render(request, 'booking/room_detail.html', context)

def book_room(request, room_id):
    """Handle room booking"""
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            
            # Check if room is available for the selected dates
            if room.is_available_for_dates(booking.check_in_date, booking.check_out_date):
                if booking.number_of_guests > room.capacity:
                    messages.error(request, f'This room can only accommodate {room.capacity} guests.')
                else:
                    booking.save()
                    messages.success(request, 'Your booking has been confirmed!')
                    return redirect('booking:booking_success', booking_id=booking.id)
            else:
                messages.error(request, 'Room is not available for the selected dates.')
    else:
        form = BookingForm()
    
    context = {
        'room': room,
        'form': form,
    }
    return render(request, 'booking/book_room.html', context)

def booking_success(request, booking_id):
    """Display booking confirmation"""
    booking = get_object_or_404(Booking, id=booking_id)
    
    context = {
        'booking': booking,
    }
    return render(request, 'booking/booking_success.html', context)
