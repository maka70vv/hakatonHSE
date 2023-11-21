from django.db import models


# Create your models here.
class Okno(models.Model):
    opened = models.BooleanField(default=False)
    