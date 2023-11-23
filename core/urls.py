from django.urls import path
from .views import DevicesView, WindowsView, RegisterView, DevicesByUserView

urlpatterns = [
    path("arduino-devices/", DevicesView.as_view()),
    path("user-devices/", WindowsView.as_view()),
    path("current-user-devices/", DevicesByUserView.as_view()),
    path('register/', RegisterView.as_view()),

]
