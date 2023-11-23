from django.db import models
from django.contrib.auth.models import User  # Импортируем модель пользователя Django


class ArduinoDevices(models.Model):
    numArduino = models.CharField(max_length=100)
    isOkno = models.BooleanField()


class Windows(models.Model):
    numArduino = models.CharField(max_length=100)
    idDevice = models.ForeignKey(
        ArduinoDevices,
        on_delete=models.CASCADE,
        related_name="windows",
        null=True
    )
    windowName = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Rooms(models.Model):
    numArduino = models.CharField(max_length=100)
    idDevice = models.ForeignKey(
        ArduinoDevices,
        on_delete=models.CASCADE,
        related_name="rooms",
        null=True
    )
    roomName = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
