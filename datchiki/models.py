from django.db import models

from arduino.models import Windows, Rooms


# Create your models here.
class WindowInfo(models.Model):
    idWindow = models.OneToOneField(
        Windows,
        on_delete=models.SET_NULL,
        related_name="okoshko",
        null=True
    )
    opened = models.BooleanField(default=False)


class RoomInfo(models.Model):
    idRoom = models.OneToOneField(
        Rooms,
        on_delete=models.SET_NULL,
        related_name="komnatka",
        null=True
    )
    temperature = models.FloatField()
    vlazhnost = models.FloatField()
    gaz = models.FloatField()
    