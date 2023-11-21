from rest_framework import serializers

from arduino.models import ArduinoDevices, Windows, Rooms


class ArduinoDevicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArduinoDevices
        fields = '__all__'


class WindowsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Windows
        fields = '__all__'


class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
