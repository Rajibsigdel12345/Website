from django.db import models
from django.contrib.auth.models import User
from hotelinfo.models import Hotel
from django.urls import reverse

# Create your models here.
# def roomvalidator(roomnumber,pk):


class RoomCharge(models.Model):
    room = models.OneToOneField(
        'Room', on_delete=models.SET_NULL, null=True)
    chargeName = models.ManyToManyField(
        'Charges')
    charge_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.charge_amount}$"

    def getcharge(self):
        return self.charge_amount


class Charges(models.Model):
    charges_choice = (("Service charge", "Service charge"),
                      ("Food charge", "Food charge"))
    name = models.CharField(max_length=50, choices=charges_choice)

    def __str__(self):
        return self.name

    def Total_charge(self):
        qs = self.roomcharge_set.prefetch_related()
        ls = [x for x in qs]
        return ls


class Room(models.Model):
    room_choice = (("Normal", "Normal"),
                   ("Suite", "Suite"), ("Deluxe", "Deluxe"))
    room_number = models.IntegerField()
    room_style = models.CharField(max_length=20, choices=room_choice)
    booking_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["room_number", "hotel"], name="unique room"
            )
        ]

    def __str__(self):
        return self.hotel.name + " "+str(self.room_number)

    def getRoomnumber(self):
        return self.room_number

    def getRoomstyle(self):
        return self.room_style

    def getBookingprice(self):
        return self.booking_price

    def getInvoice(self):
        return self.getRoomcharge()

    def getRoomcharge(self):
        return self.roomcharge

    def get_absolute_url(self):
        return reverse('hotelinfo:Room', args=[str(self.hotel.pk)])


class Invoice(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    charges = models.ManyToManyField(
        RoomCharge, related_name="invoice_set")

    def __str__(self):
        qs = self.room.getInvoice()
        return f'{qs}'

    def getRoom(self):
        return (self.room.room_number)

    def Hotel(self):
        return self.room.hotel.name


class RoomKey(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return f'{str(self.room.getRoomnumber())} {self.barcode}'


class RoomBooking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Guest_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_Nights = models.IntegerField()


class RoomHouseKeeping(models.Model):
    status_choice = (
        ("Available", "Available"), ("Unavailable", "Unavailable"), ("Pending", "Wait"))
    room = models.ManyToManyField("Room")
    date = models.DateField()
    status = models.CharField(max_length=20, choices=status_choice)

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
