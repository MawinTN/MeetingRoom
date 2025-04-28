from django.db import models

class RoomBooking(models.Model):
    name = models.CharField(max_length=100)
    room_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.room_name}"
