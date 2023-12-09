from django.db import models
from django.contrib.auth.models import User


class ArduinoDevices(models.Model):
    numArduino = models.CharField(max_length=100)
    isWindow = models.BooleanField(default=False)


class Devices(models.Model):
    numArduino = models.CharField(max_length=100)
    idDevice = models.ForeignKey(
        ArduinoDevices,
        on_delete=models.CASCADE,
        related_name="windows",
        null=True
    )
    name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    temperature = models.FloatField(default=0)
    vlazhnost = models.FloatField(default=0)
    gaz = models.FloatField(default=0)
    windowsAreOpened = models.BooleanField(default=False)
    windowsAreBlocked = models.BooleanField(default=False)
