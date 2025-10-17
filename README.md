# Hotel Booking System

A simple hotel booking system built with Django that allows users to browse available rooms, view room details, and make reservations.

## Features Implemented

### Core Features

- **List All Available Rooms**: Browse through all available hotel rooms with a clean, card-based layout
- **View Room Details**: Click on any room to see detailed information including price, capacity, location, and description
- **Book a Room**: Fill out a booking form with guest information and preferred dates
- **Admin Panel**: Manage rooms and bookings through Django's admin interface
- **SQLite Database**: All data is stored in a lightweight SQLite database
- **Responsive Templates**: Modern, mobile-friendly design using Bootstrap 5

### Bonus Features

- **Search and Filter**: Search rooms by:
  - Room type (Single, Double, Suite, Deluxe)
  - Location
  - Maximum price per night
- **Booking Validation**: Prevents double bookings and validates guest capacity
- **Price Calculation**: Automatically calculates total price based on number of nights

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or navigate to the project directory**

   ```bash
   cd hotel_booking_project
   ```

2. **Activate the virtual environment**

   ```bash
   # On macOS/Linux
   source ../venv/bin/activate

   # On Windows
   ..\venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (if not already done)

   ```bash
   python manage.py migrate
   ```

5. **Create sample room data** (if not already done)

   ```bash
   python manage.py populate_rooms
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`
- **Email**: `admin@example.com`

## Project Structure

```
hotel_booking_project/
├── booking/                  # Main Django app
│   ├── models.py            # Room and Booking models
│   ├── views.py             # View functions
│   ├── forms.py             # Booking and search forms
│   ├── admin.py             # Admin configurations
│   ├── urls.py              # URL patterns
│   └── management/          # Custom management commands
│       └── commands/
│           └── populate_rooms.py
├── templates/               # HTML templates
│   ├── base.html           # Base template with navigation
│   └── booking/
│       ├── room_list.html       # Room listing page
│       ├── room_detail.html     # Room details page
│       ├── book_room.html       # Booking form
│       └── booking_success.html # Booking confirmation
├── hotel_booking_project/   # Project settings
│   ├── settings.py
│   └── urls.py
├── requirements.txt         # Python dependencies
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

## Usage Guide

1. **Browse Rooms**: Visit the homepage to see all available rooms
2. **Search Rooms**: Use the search form to filter by room type, location, or price
3. **View Details**: Click on any room card to see full details
4. **Make a Booking**: Click "Book Now" and fill out the guest information form
5. **Admin Management**: Log into the admin panel to:
   - Add/edit/delete rooms
   - View and manage bookings
   - Change room availability

## Sample Data

The system comes pre-populated with 8 sample rooms:

- 2 Single rooms ($99.99/night)
- 2 Double rooms ($149.99-$159.99/night)
- 2 Suite rooms ($299.99-$329.99/night)
- 2 Deluxe rooms ($449.99-$499.99/night)

## Technologies Used

- **Backend**: Django 5.2.3
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap 5.1.3
- **Icons**: Font Awesome 6.0.0
- **Python**: 3.x

## Notes

- This is a development setup. For production, update `SECRET_KEY`, set `DEBUG=False`, and use a production database
- Email notifications are not actually sent (shown as confirmation only)
- The system prevents double bookings for the same dates
