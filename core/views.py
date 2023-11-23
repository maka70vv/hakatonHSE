from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes

from .models import ArduinoDevices, Devices
from .serializers import ArduinoDevicesSerializers, DevicesSerializers, RegisterSerializer, \
    UserSerializer, WindowsListSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
        })


class DevicesView(generics.ListCreateAPIView):
    queryset = ArduinoDevices.objects.all()
    serializer_class = ArduinoDevicesSerializers
    permission_classes = [permissions.IsAuthenticated]


class DevicesByUserView(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = WindowsListSerializer
    permission_classes = [permissions.IsAuthenticated]


class WindowsView(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializers
    permission_classes = [permissions.IsAuthenticated]


class DevicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializers
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"error": "Нет прав для удаления этого устройства"}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def toggle_windows_status(request, device_id):
    try:
        device = Devices.objects.get(pk=device_id, user=request.user)
    except Devices.DoesNotExist:
        return Response({"error": "Устройство не найдено"}, status=status.HTTP_404_NOT_FOUND)

    if not device.windowsAreBlocked and not device.windowsAreOpened:
        device.windowsAreOpened = True
        device.save()
        serializer = DevicesSerializers(device)
        return Response(serializer.data)
    elif device.windowsAreOpened:
        device.windowsAreOpened = False
        device.save()
        serializer = DevicesSerializers(device)
        return Response(serializer.data)
    elif not device.windowsAreOpened and device.windowsAreBlocked:
        return Response({"error": "Окна заблокированы, невозможно открыть"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def block_windows(request, device_id):
    try:
        device = Devices.objects.get(pk=device_id, user=request.user)
    except Devices.DoesNotExist:
        return Response({"error": "Устройство не найдено"}, status=status.HTTP_404_NOT_FOUND)

    if not device.windowsAreBlocked and not device.windowsAreOpened:
        device.windowsAreBlocked = True
        device.save()
        serializer = DevicesSerializers(device)
        return Response(serializer.data)
    elif not device.windowsAreOpened and device.windowsAreBlocked:
        device.windowsAreBlocked = False
        device.save()
        serializer = DevicesSerializers(device)
        return Response(serializer.data)
    elif device.windowsAreOpened and not device.windowsAreBlocked:
        return Response({"error": "Окна открыты! Закройте, чтобы заблокировать"}, status=status.HTTP_400_BAD_REQUEST)
