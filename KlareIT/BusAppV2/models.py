from django.db import models

class Busapp(models.Model):
    bus_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    fare = models.DecimalField(max_digits=6, decimal_places=2)
    departure_time = models.TimeField(auto_now=True)
    bustype = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_name