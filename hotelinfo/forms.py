from django.forms import ModelForm
from hotel.models import RoomBooking


class bookroomForm(ModelForm):
    class Meta:
        model = RoomBooking
        fields = "__all__"
