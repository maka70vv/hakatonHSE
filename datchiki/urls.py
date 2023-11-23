from django.urls import path
from .views import WindowInfoView, RoomInfoView

urlpatterns = [
    path("window-info/", WindowInfoView.as_view()),
    path("room-info/", RoomInfoView.as_view()),
]
