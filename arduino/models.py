from django.db import models


class ArduinoDevices(models.Model):
    numArduino = models.CharField(max_length=100)
    isOkno = models.BooleanField()


class Windows(models.Model):
    numArduino = models.CharField(max_length=100)
    idDevice = models.ForeignKey(
        ArduinoDevices,
        on_delete=models.CASCADE,
        related_name="windows"
    )
    windowName = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if not self.numArduino:
            existing_device = ArduinoDevices.objects.filter(numArduino=self.numArduino, isOkno=True).first()

            if existing_device:
                self.idDevice = existing_device

        super().save(*args, **kwargs)


class Rooms(models.Model):
    numArduino = models.CharField(max_length=100)
    idDevice = models.ForeignKey(
        ArduinoDevices,
        on_delete=models.CASCADE,
        related_name="rooms"
    )
    roomName = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.numArduino:
            existing_device = ArduinoDevices.objects.filter(numArduino=self.numArduino, isOkno=False).first()

            if existing_device:
                self.idDevice = existing_device

        super().save(*args, **kwargs)
