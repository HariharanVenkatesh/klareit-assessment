from django.db import models
class genderoption(models.TextChoices):
   MALE = 'M', 'Male'
   FEMALE = 'F', 'Female'
   TRANSGENDER = 'T', 'Transgender'
   Unidentified = 'U','Unidentified'


class BusApp(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=genderoption.choices, default=genderoption.Unidentified)
    pickuppoint = models.CharField(max_length=100)
    droppoint = models.CharField(max_length=100)
    totaldistance = models.IntegerField(default =0)
    dateandtime = models.DateTimeField(auto_now=True)
    ticketprice = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.name
