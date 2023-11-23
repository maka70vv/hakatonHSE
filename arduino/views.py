from rest_framework import generics
from .models import ArduinoDevices, Windows, Rooms
from .serializers import ArduinoDevicesSerializers, WindowsSerializers, RoomsSerializers, RegisterSerializer, \
    UserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
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


class WindowsView(generics.ListCreateAPIView):
    queryset = Windows.objects.all()
    serializer_class = WindowsSerializers
    permission_classes = [permissions.IsAuthenticated]


class RoomsView(generics.ListCreateAPIView):
    queryset = Rooms
    serializer_class = RoomsSerializers
    permission_classes = [permissions.IsAuthenticated]
