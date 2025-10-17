from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('room/<int:room_id>/book/', views.book_room, name='book_room'),
    path('booking/<int:booking_id>/success/', views.booking_success, name='booking_success'),
] 