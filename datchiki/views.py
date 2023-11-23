from rest_framework import generics

from datchiki.models import WindowInfo, RoomInfo
from datchiki.serializers import WindowInfoSerializers, RoomInfoSerializers


class WindowInfoView(generics.ListCreateAPIView):
    queryset = WindowInfo.objects.all()
    serializer_class = WindowInfoSerializers


class RoomInfoView(generics.ListCreateAPIView):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomInfoSerializers
