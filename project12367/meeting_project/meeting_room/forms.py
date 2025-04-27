from django import forms
from .models import RoomBooking

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['name', 'room_name', 'booking_date', 'start_time', 'end_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'room_name': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }