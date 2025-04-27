from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),  # หน้ารายการจอง
    path('add/', views.add_booking, name='add_booking'),  # เพิ่มการจอง
    path('edit/<int:pk>/', views.edit_booking, name='edit_booking'),  # แก้ไขการจอง
    path('delete/<int:pk>/', views.delete_booking, name='delete_booking'),  # ลบการจอง
]