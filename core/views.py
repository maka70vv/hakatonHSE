import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def update_device(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            num_arduino = data.get('numArduino')
            temperature = data.get('temperature')
            vlazhnost = data.get('vlazhnost')
            gaz = data.get('gaz')

            device = Devices.objects.get(numArduino=num_arduino)
            device.temperature = temperature
            device.vlazhnost = vlazhnost
            device.gaz = gaz

            if temperature > 30 and not device.windowsAreBlocked and not device.windowsAreOpened:
                device.windowsAreOpened = True
            elif temperature < 20 and device.windowsAreOpened:
                device.windowsAreOpened = False
            elif vlazhnost > 50 and not device.windowsAreBlocked and not device.windowsAreOpened:
                device.windowsAreOpened = True
            elif vlazhnost < 30 and device.windowsAreOpened:
                device.windowsAreOpened = False
            elif gaz > 1.5 and not device.windowsAreBlocked and not device.windowsAreOpened:
                device.windowsAreOpened = True
            elif gaz < 0.5 and device.windowsAreOpened:
                device.windowsAreOpened = False
            elif gaz > 3 and not device.windowsAreOpened:
                device.windowsAreOpened = True

            device.save()

            return JsonResponse({'status': 'success'})
        except Devices.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Устройство не найдено'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})
