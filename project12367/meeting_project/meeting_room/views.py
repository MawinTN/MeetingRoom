from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomBooking
from .forms import RoomBookingForm
from django.db.models import Q  # เพิ่ม Q สำหรับการค้นหาแบบ OR
from django.utils.timezone import now  # สำหรับดึงเวลาปัจจุบัน

def booking_list(request):
    query = request.GET.get('q')  # รับค่าจากช่องค้นหา
    if query:
        bookings = RoomBooking.objects.filter(
            Q(name__icontains=query) |  # ค้นหาตามชื่อผู้จอง
            Q(room_name__icontains=query) |  # ค้นหาตามชื่อห้อง
            Q(booking_date__icontains=query)  # ค้นหาตามวันที่จอง
        )
    else:
        bookings = RoomBooking.objects.all()
    return render(request, 'meeting_room/booking_list.html', {'bookings': bookings})

def add_booking(request):
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # กลับไปยังหน้ารายการจอง
    else:
        form = RoomBookingForm()
    return render(request, 'meeting_room/add_booking.html', {'form': form})

def edit_booking(request, pk):
    booking = get_object_or_404(RoomBooking, pk=pk)
    if request.method == 'POST':
        form = RoomBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')  # กลับไปยังหน้ารายการจอง
    else:
        form = RoomBookingForm(instance=booking)
    return render(request, 'meeting_room/edit_booking.html', {'form': form})

def delete_booking(request, pk):
    booking = get_object_or_404(RoomBooking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')  # กลับไปยังหน้ารายการจอง
    return render(request, 'meeting_room/delete_booking.html', {'booking': booking})

def room_status(request):
    rooms = ['Room 1', 'Room 2', 'Room 3']  # รายชื่อห้องประชุม
    current_time = now()

    room_status_list = []
    for room in rooms:
        # ตรวจสอบว่าห้องนี้มีการจองในเวลาปัจจุบันหรือไม่
        is_occupied = RoomBooking.objects.filter(
            room_name=room,
            booking_date=current_time.date(),
            start_time__lte=current_time.time(),
            end_time__gte=current_time.time()
        ).exists()

        room_status_list.append({
            'room_name': room,
            'status': 'ไม่ว่าง' if is_occupied else 'ว่าง'
        })

    return render(request, 'meeting_room/room_status.html', {'room_status_list': room_status_list})
