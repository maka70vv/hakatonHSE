from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import ArduinoDevices, Devices


class ArduinoDevicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArduinoDevices
        fields = '__all__'


class DevicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        num_arduino = validated_data.get('numArduino')
        existing_device = ArduinoDevices.objects.filter(numArduino=num_arduino).first()

        if existing_device:
            validated_data['idDevice'] = existing_device
            return super().create(validated_data)
        else:
            raise ValidationError("Устройство с номером платы Arduino не найдено")


class WindowsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

    def to_representation(self, instance):
        user = self.context['request'].user
        if instance.user == user:
            return super().to_representation(instance)
        else:
            return serializers.Serializer({"name": "chuzhoi"})


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return data

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
