from rest_framework import generics
from .models import ArduinoDevices, Windows, Rooms
from .serializers import ArduinoDevicesSerializers, WindowsSerializers, RoomsSerializers


class DevicesView(generics.ListCreateAPIView):
    queryset = ArduinoDevices.objects.all()
    serializer_class = ArduinoDevicesSerializers


class WindowsView(generics.ListCreateAPIView):
    queryset = Windows.objects.all()
    serializer_class = WindowsSerializers


class RoomsView(generics.ListCreateAPIView):
    queryset = Rooms
    serializer_class = RoomsSerializers
