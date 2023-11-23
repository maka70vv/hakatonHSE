from django.urls import path
from .views import DevicesView, WindowsView, RegisterView, DevicesByUserView, DevicesDetailView, toggle_windows_status, \
    block_windows

urlpatterns = [
    path("arduino-devices/", DevicesView.as_view()),
    path("user-devices/", WindowsView.as_view()),
    path("current-user-devices/", DevicesByUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('user-devices/<int:pk>/', DevicesDetailView.as_view()),
    path('windows_open/<int:device_id>/', toggle_windows_status),
    path('windows_block/<int:device_id>/', block_windows),
]
