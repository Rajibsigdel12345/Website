from django.contrib import admin
from django.apps import apps
from .models import Hotel, HotelLocation, Account


class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "__str__", 'getRoom']


class HotelLocationAdmin(admin.ModelAdmin):
    list_display = ["location", "address", "phone"]


class AccountAdmin(admin.ModelAdmin):
    list_display = ["username", "actype"]


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelLocation, HotelLocationAdmin)
admin.site.register(Account, AccountAdmin)


# Register your models here.
