from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class BusStation(models.Model):
    name = models.CharField(max_length=60, blank=False)


class Routes(models.Model):
    number = models.IntegerField(default=0)
    stations = ArrayField(models.CharField(max_length=60))


class PassengerBit(models.Model):
    current_time = models.TimeField()
    current_data = models.DateField()
    bus_station = models.CharField(max_length=60)
    route_number = models.IntegerField()

