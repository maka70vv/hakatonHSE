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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Добавляем поле для пользователя

    def save(self, *args, **kwargs):
        if not self.idDevice and self.numArduino:
            existing_device = ArduinoDevices.objects.filter(numArduino=self.numArduino).first()

            if existing_device:
                self.idDevice = existing_device
                self.user = existing_device.user

        super().save(*args, **kwargs)


class Rooms(models.Model):
    numArduino = models.CharField(max_length=100)
    idDevice = models.ForeignKey(
        ArduinoDevices,
        on_delete=models.CASCADE,
        related_name="rooms",
        null=True
    )
    roomName = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Добавляем поле для пользователя

    def save(self, *args, **kwargs):
        if not self.numArduino:
            existing_device = ArduinoDevices.objects.filter(numArduino=self.numArduino).first()

            if existing_device:
                self.idDevice = existing_device
                self.user = existing_device.user  # Записываем пользователя, который отправил элемент

        super().save(*args, **kwargs)
