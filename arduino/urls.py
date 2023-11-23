from django.urls import path
from .views import DevicesView, WindowsView, RoomsView, RegisterView

urlpatterns = [
    path("devices/", DevicesView.as_view()),
    path("windows/", WindowsView.as_view()),
    path("rooms/", RoomsView.as_view()),
    path('register/', RegisterView.as_view()),

]
