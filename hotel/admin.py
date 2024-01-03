from django.contrib import admin
from django.apps import apps
from .models import Room, RoomCharge, Charges, Invoice


class RoomAdmin(admin.ModelAdmin):
    list_display = ['__str__', "room_style",
                    "booking_price", 'getRoomcharge', 'getInvoice']


admin.site.register(Room, RoomAdmin)


class RoomChargeAdmin(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(RoomCharge, RoomChargeAdmin)


class ChargesAdmin(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(Charges, ChargesAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'getRoom', 'Hotel']


admin.site.register(Invoice, InvoiceAdmin)
post_models = apps.get_app_config('hotel').get_models()

for model in post_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
# Register your models here.
