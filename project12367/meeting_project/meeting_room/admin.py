from django.contrib import admin
from .models import RoomBooking

@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_name', 'booking_date', 'start_time', 'end_time')
