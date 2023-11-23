from rest_framework import serializers
from datchiki.models import WindowInfo, RoomInfo


class WindowInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = WindowInfo
        fields = '__all__'


class RoomInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomInfo
        fields = '__all__'
