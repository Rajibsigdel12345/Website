from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HotelLocation(models.Model):
    location = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __str__(self):
        return self.location


class Hotel(models.Model):
    locations = models.ManyToManyField(
        HotelLocation)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=255)
    Total_rooms = models.IntegerField()

    def __str__(self):
        return self.name

    def getRoom(self):
        return self.room_set.select_related("hotel")

    def get_absolute_url(self):
        return f'/{self.pk}/'


class Account(models.Model):
    account_choice = (("GUEST", "GUEST"), ("RECEPTIONIST", "RECEPTIONIST"),
                      ("HOUSEKEEPING", "HOUSEKEEPING"), ("SERVER", "SERVER"))
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    actype = models.CharField(max_length=25, choices=account_choice)

    def __str__(self) -> str:
        return self.actype
