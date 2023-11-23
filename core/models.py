from django.db import models
from django.contrib.auth.models import User


class ArduinoDevices(models.Model):
    numArduino = models.CharField(max_length=100)


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
    temperature = models.FloatField(null=True),
    vlazhnost = models.FloatField(null=True),
    gaz = models.FloatField(null=True),
    windowsAreOpened = models.BooleanField(default=False)
    windowsAreBlocked = models.BooleanField(default=False)
