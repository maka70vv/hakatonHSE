from django.urls import path
from .views import DevicesView, WindowsView, RegisterView, DevicesByUserView, DevicesDetailView, \
    toggle_windows_status, block_windows, update_device

urlpatterns = [
    path("arduino-devices/", DevicesView.as_view()),
    path("user-devices/", WindowsView.as_view()),
    path("current-user-devices/", DevicesByUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('user-devices/<int:pk>/', DevicesDetailView.as_view()),
    path('windows-open/<int:device_id>/', toggle_windows_status),
    path('windows-block/<int:device_id>/', block_windows),
    path('update-data/', update_device)
]
