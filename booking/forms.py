from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'guest_phone', 'check_in_date', 
                  'check_out_date', 'number_of_guests', 'special_requests']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'check_out_date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
            'guest_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'guest_email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
            'guest_phone': forms.TextInput(attrs={'placeholder': '+1 234 567 8900'}),
            'number_of_guests': forms.NumberInput(attrs={'min': 1}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['special_requests']:
                self.fields[field].required = True
                
class RoomSearchForm(forms.Form):
    ROOM_TYPE_CHOICES = [('', 'All Types')] + [(t[0], t[1]) for t in [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
    ]]
    
    room_type = forms.ChoiceField(choices=ROOM_TYPE_CHOICES, required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=100, required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}))
    max_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False,
                                  widget=forms.NumberInput(attrs={'placeholder': 'Max Price', 'class': 'form-control', 'min': 0})) 